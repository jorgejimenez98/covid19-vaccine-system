from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.main.decorators import checkUserAccess
from apps.main.errorFunctions import *
from ..models import Vaccine, School_Vaccination
from ..formClass import SchoolVaccineForm
from apps.people.models import People
from apps.people.formClass import PersonForm
from apps.locality.models import School

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
    personForm = PersonForm()
    personForm.updateValues(person)
    # Init Context
    context = {
        "person": personForm,
        "vaccines": Vaccine.objects.filter(canSchool=True),
        "schools": School.objects.all(),
        "vaccination": SchoolVaccineForm()
    }
    if request.method == 'POST':
        # Get data from template
        valVaccineId = request.POST.get('val_vaccine')
        valBadReactions = request.POST.get('val_badReaction') == 'on'
        val_schoolId = request.POST.get('val_school')
        # Update Context
        context['vaccination'].vaccineId = valVaccineId
        context['vaccination'].badReaction = valBadReactions
        context['vaccination'].schoolId = val_schoolId
        try:
            # Create Vaccination
            School_Vaccination.objects.create(
                people=person,
                vaccine=Vaccine.objects.get(pk=int(valVaccineId)),
                has_adverse_reactions=valBadReactions,
                school=School.objects.get(pk=int(val_schoolId))
            )
            messages.success(request, getSuccessCreatedMessage('Vacunacion'))
            return redirect(f'/person/vaccines/{person.id}')
        except Exception as e:
            messages.error(request, e.args[0])
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
