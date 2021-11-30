from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.main.decorators import checkUserAccess
from apps.main.errorFunctions import *
from ..models import Vaccine, School_Vaccination, PersonalHealth_Vaccination, ConsultingRoom_Vaccination, Doce
from ..formClass import SchoolVaccineForm, ConsultginVaccineForm, HealthVaccineForm
from apps.people.models import People
from apps.people.formClass import PersonForm
from apps.locality.models import School, ConsultingRoom


def getVaccine(vaccineId, vaccine):
    obj = None
    if vaccine == 'VacunaPersonalSalud':
        obj = PersonalHealth_Vaccination.objects.get(pk=int(vaccineId))
    elif vaccine == 'VacunaConsultorio':
        obj = ConsultingRoom_Vaccination.objects.get(pk=int(vaccineId))
    elif vaccine == 'VacunaEscuelas':
        obj = School_Vaccination.objects.get(pk=int(vaccineId))
    return obj


@login_required(login_url='/login')
@checkUserAccess(rol='SPECIALIST', error_url='/403')
def personVaccinesDocesList(request, pk, vaccine, vaccineId):
    person = People.objects.get(pk=pk)
    vaccine = getVaccine(vaccineId, vaccine)
    context = {
        "person": person,
        "vaccine": vaccine,
        "doces": vaccine.doses.all(),
    }
    return render(request, 'vaccines/doceList.html', context)


@login_required(login_url='/login')
@checkUserAccess(rol='SPECIALIST', error_url='/403')
def personVaccinesDocesAdd(request, pk, vaccine, vaccineId):
    person = People.objects.get(pk=pk)
    vaccine = getVaccine(vaccineId, vaccine)
    context = {
        "person": person,
        "vaccine": vaccine,
        "doces": vaccine.doses.all(),
    }
    if request.method == 'POST':
        val_lot = request.POST.get('val_name')
        try:
            Doce.objects.create(
                lot=val_lot,
                vaccination=vaccine   
            )
            messages.success(request, getSuccessCreatedMessage("Dosis"))
            return redirect(f'/person/vaccines/doces/{pk}/{vaccine.tipoVacuna()}/{vaccineId}/')
        except Exception as e:
            messages.error(request, e.args[0])
    return render(request, 'vaccines/addLote.html', context)


@login_required(login_url='/login')
@checkUserAccess(rol='SPECIALIST', error_url='/403')
def personVaccinesDocesDelete(request, pk, vaccine, vaccineId, doceId):
    doce = Doce.objects.get(pk=doceId)
    try:  
        doce.delete()
        messages.success(request, getDeleSuccessText("Dosis"))
    except Exception as e:
        messages.error(request, e.args[0])
    return redirect(f'/person/vaccines/doces/{pk}/{vaccine}/{vaccineId}/')
