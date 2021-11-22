from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.db.models import ProtectedError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.main.decorators import checkUserAccess
from apps.main.errorFunctions import *
from ..formClass import MunicipalityForm
from ..models import Municipality, Province


""" Municipality LIST """


@login_required(login_url='/login')
@checkUserAccess(rol='ADMIN', error_url='/403')
def municipalityListView(request):
    # Init Context
    context = {"municipalities": Municipality.objects.all().order_by('-pk')}
    # Render List
    return render(request, 'municipality/list.html', context)


""" ADD Municipality """


@login_required(login_url='/login')
@checkUserAccess(rol='ADMIN', error_url='/403')
def municipalityAddView(request):
    # Init Context
    context = {
        "mun": MunicipalityForm(None, "", "", ""),
        "provinces": Province.objects.all().order_by('-pk')
    }
    # Render Mun Form
    if request.method == 'POST':
        # Get data from template
        name = request.POST.get("val_name")
        val_province_id = request.POST.get("val_province_id")
        # Update context
        context['mun'].name = name
        context['mun'].provinceId = val_province_id
        try:
            # Create Mun
            Municipality.objects.create(
                name=name,
                province=Province.objects.get(pk=int(val_province_id))
            )
            # Redirect MUN List
            messages.success(request, getSuccessCreatedMessage('Municipio'))
            return redirect("municipalityListView")
        except Exception as e:
            # Validate all posible errors
            messages.error(request, e.args[0])
    return render(request, 'municipality/add.html', context)
