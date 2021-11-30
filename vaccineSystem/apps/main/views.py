from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .errorFunctions import *

# Models
from django.contrib.auth import get_user_model
from ..people.models import People
from ..vaccine.models import Vaccine, School_Vaccination, ConsultingRoom_Vaccination, PersonalHealth_Vaccination


def homeView(request):
    if not request.user.is_authenticated:
        return redirect('loginView')
    return redirect('dashboardView')


def logoutView(request):
    logout(request)
    return redirect('homeView')


def error404View(request):
    return render(request, 'error403.html')


def loginView(request):
    # Init Context
    context = {"username": "", "password": ""}
    if request.method == 'POST':
        # Get Data from template
        username = request.POST.get('val_username')
        password = request.POST.get('val_password')
        try:
            # Update context
            context['username'] = username
            context['password'] = password
            # Get user
            user = get_user_model().objects.get(username=username)
            # Check password
            if not user.check_password(password):
                messages.error(request, 'Contraseña incorrecta')
            else:
                # Login User
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('dashboardView')
        except get_user_model().DoesNotExist as e:
            # Send error if user does not exist
            messages.error(request, getNotExistUserError(username))
        except Exception as e:
            # Check all posible errors
            messages.error(request, e.args[0])
    # Render to login page
    return render(request, 'login.html', context)


def getNumberOfVaccinations():
    return School_Vaccination.objects.all().count() + ConsultingRoom_Vaccination.objects.all().count() + PersonalHealth_Vaccination.objects.all().count()


@login_required(login_url='/login')
def dashboardView(request):
    context = {
        "users": get_user_model().objects.all().count(),
        "persons": People.objects.all().count(),
        "vaccines": Vaccine.objects.all().count(),
        "vaccinations": getNumberOfVaccinations()
    }
    return render(request, 'home.html', context)
