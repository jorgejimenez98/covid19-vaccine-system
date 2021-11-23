from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.db.models import ProtectedError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.main.decorators import checkUserAccess
from apps.main.errorFunctions import *
from ..formClass import SchoolForm
from ..models import Municipality, Polyclinic


""" POLYCLINIC LIST """


@login_required(login_url='/login')
@checkUserAccess(rol='ADMIN', error_url='/403')
def polyclinicListView(request):
    # Init Context
    context = {"polyclinics": Polyclinic.objects.all().order_by('-pk')}
    # Render List
    return render(request, 'polyclinic/list.html', context)


""" ADD SCHOOLS """


@login_required(login_url='/login')
@checkUserAccess(rol='ADMIN', error_url='/403')
def polyclinicAddView(request):
    # Init Context
    context = {
        "pol": SchoolForm(None, "", "", ""),
        "muns": Municipality.objects.all().order_by('-pk')
    }
    # Render Mun Form
    if request.method == 'POST':
        # Get data from template
        name = request.POST.get("val_name")
        val_mun_id = request.POST.get("val_mun_id")
        # Update context
        context['pol'].name = name
        context['pol'].munId = val_mun_id
        try:
            # Create Schools
            Polyclinic.objects.create(
                name=name,
                municipality=Municipality.objects.get(pk=int(val_mun_id))
            )
            # Redirect MUN List
            messages.success(request, getSuccessCreatedMessage('Policlinico'))
            return redirect("polyclinicListView")
        except Exception as e:
            # Validate all posible errors
            messages.error(request, e.args[0])
    return render(request, 'polyclinic/addOrEdit.html', context)
