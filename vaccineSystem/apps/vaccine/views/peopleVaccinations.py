from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.main.decorators import checkUserAccess
from apps.main.errorFunctions import *
from ..models import Vaccine
from apps.people.models import People
from ..formClass import VaccineForm


""" VACCINE LIST """


@login_required(login_url='/login')
@checkUserAccess(rol='SPECIALIST', error_url='/403')
def personVaccinesList(request, pk):
    person = People.objects.get(pk=pk)
    # Init Context
    context = {
        "person": person,
        "vaccines": person.vaccinations.all(),
    }
    # Render to vaccine List
    return render(request, 'vaccines/personVaccines.html', context)


""" School VACCINE ADD """


@login_required(login_url='/login')
@checkUserAccess(rol='SPECIALIST', error_url='/403')
def personAddSchoolVaccine(request, pk):
    person = People.objects.get(pk=pk)
    # Init Context
    context = {
        "person": person,
    }
    # Render to vaccine List
    return render(request, 'vaccines/addSchoolVaccine.html', context)


""" School VACCINE ADD """


@login_required(login_url='/login')
@checkUserAccess(rol='SPECIALIST', error_url='/403')
def personAddConsultVaccine(request, pk):
    person = People.objects.get(pk=pk)
    # Init Context
    context = {
        "person": person,
    }
    # Render to vaccine List
    return render(request, 'vaccines/addConsultVaccine.html', context)


""" Health VACCINE ADD """


@login_required(login_url='/login')
@checkUserAccess(rol='SPECIALIST', error_url='/403')
def personAddHealthVaccine(request, pk):
    person = People.objects.get(pk=pk)
    # Init Context
    context = {
        "person": person,
    }
    # Render to vaccine List
    return render(request, 'vaccines/addHealthVaccine.html', context)
