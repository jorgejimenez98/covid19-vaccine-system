from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .formClass import VaccineForm
from ..main.decorators import checkUserAccess
from ..main.errorFunctions import *
from .models import Vaccine


""" VACCINE LIST """


@login_required(login_url='/login')
@checkUserAccess(rol='ADMIN', error_url='/403')
def vaccinesListView(request):
    # Init Context
    context = {"vaccines": Vaccine.objects.all().order_by('-pk')}
    # Render to vaccine List
    return render(request, 'vaccines/list.html', context)


""" VACCINE ADD """


@login_required(login_url='/login')
@checkUserAccess(rol='ADMIN', error_url='/403')
def vaccinesAddView(request):
    # Init Context
    context = {"vaccine": VaccineForm(None, "", False, False, False)}
    # Render User Form
    if request.method == 'POST':
        # Get data from template
        name = request.POST.get("val_name")
        healthPersonnel = request.POST.get("val_healthPersonnel")
        canConsultingRoom = request.POST.get("val_canConsultingRoom")
        canSchool = request.POST.get("val_canSchool")
        # Update context
        context['vaccine'].name = name
        context['vaccine'].healthPersonnel = healthPersonnel
        context['vaccine'].canConsultingRoom = canConsultingRoom
        context['vaccine'].canSchool = canSchool
        try:
            # Validate boolean fields
            if [healthPersonnel, canConsultingRoom, canSchool].count('on') in [3, 2, 0]:
                raise Exception(getOnlyOneBoolError())
            # Create Model
            Vaccine.objects.create(
                name=name,
                healthPersonnel=healthPersonnel == 'on',
                canConsultingRoom=canConsultingRoom == 'on',
                canSchool=canSchool == 'on'
            )
            # Redirect Model List
            messages.success(request, getSuccessCreatedMessage('Vacuna'))
            return redirect("vaccinesListView")
        except ValidationError:
            # Validate Unique field
            messages.error(request, getUniqueModelError("Vacuna", name))
        except Exception as e:
            # Validate all posible errors
            messages.error(request, e.args[0])
    return render(request, 'vaccines/addOrEdit.html', context)
