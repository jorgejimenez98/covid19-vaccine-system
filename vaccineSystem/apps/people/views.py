from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.db.models import ProtectedError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..main.decorators import checkUserAccess
from ..main.errorFunctions import *
from ..locality.models import ConsultingRoom
from .models import People
from .formClass import PersonForm
import django_excel as excel


""" PERSONS LIST """


@login_required(login_url='/login')
@checkUserAccess(rol='SPECIALIST', error_url='/403')
def peopleListView(request):
    # Init Context
    context = {"persons": People.objects.all()}
    if request.method == 'POST':
        val_edad = request.POST.get('val_edad')
        if val_edad != '':
            maximaEdad, minimaEdad = 0, 0
            if '+' in val_edad:
                context['persons'] = People.objects.filter(age__gte=60)
            else:
                aux = val_edad.split('-')
                minimaEdad, maximaEdad = int(aux[0]), int(aux[1])
                context['persons'] = People.objects.filter(age__gte=minimaEdad, age__lte=maximaEdad)
    # Render List
    return render(request, 'people/list.html', context)


""" ADD PERSON """


@login_required(login_url='/login')
@checkUserAccess(rol='SPECIALIST', error_url='/403')
def peopleAddView(request):
    # Init Context
    context = {
        "person": PersonForm(),
        "consults": ConsultingRoom.objects.all()
    }
    if request.method == 'POST':
        # Get data from template
        val_ci = request.POST.get('val_ci')
        val_name = request.POST.get('val_name')
        val_last_names = request.POST.get('val_last_names')
        val_sex = request.POST.get('val_sex')
        val_age = request.POST.get('val_age')
        val_adress = request.POST.get('val_adress')
        val_consultId = request.POST.get('val_consult')
        val_prc_possitive = request.POST.get('val_prc_possitive') == 'on'
        val_date_prc = request.POST.get('val_date_prc')
        # Update context
        context['person'].ci = val_ci.strip()
        context['person'].name = val_name
        context['person'].last_names = val_last_names
        context['person'].sex = val_sex
        context['person'].age = val_age
        context['person'].address = val_adress
        context['person'].consulting_room_id = val_consultId
        context['person'].positive_pcr = val_prc_possitive
        context['person'].date_pcr = val_date_prc
        # Try execpt
        try:
            """ Validate CI """
            validateCI(str(val_ci).strip())
            # Validate pcr and date
            if val_prc_possitive and val_date_prc == '':
                raise Exception(getNoDatePcr())
            elif not val_prc_possitive and val_date_prc != '':
                raise Exception(getNoPcrSelect())
            # Create Person
            People.objects.create(
                ci=val_ci.strip(),
                name=val_name,
                last_names=val_last_names,
                sex=val_sex,
                age=int(val_age),
                address=val_adress,
                consulting_room=ConsultingRoom.objects.get(
                    pk=int(val_consultId)),
                positive_pcr=val_prc_possitive,
                date_pcr=None if val_date_prc == '' else getDateFromString(
                    val_date_prc)
            )
            # Render to list after create
            messages.success(request, getSuccessCreatedMessage("Persona"))
            return redirect('peopleListView')
        except ValidationError:
            # Validate Unique CI
            messages.error(request, getUniqueCIError("Persona", val_ci))
        except Exception as e:
            # Manage All posible Errors
            messages.error(request, e.args[0])
    # Render Form
    return render(request, 'people/addOrEdit.html', context)


""" EDIT PERSON """


@login_required(login_url='/login')
@checkUserAccess(rol='SPECIALIST', error_url='/403')
def peopleEditView(request, pk):
    # Init Context
    person = People.objects.get(id=pk)
    personForm = PersonForm()
    personForm.updateValues(person)
    context = {
        "person": personForm,
        "consults": ConsultingRoom.objects.all()
    }
    if request.method == 'POST':
        # Get data from template
        val_ci = request.POST.get('val_ci')
        val_name = request.POST.get('val_name')
        val_last_names = request.POST.get('val_last_names')
        val_sex = request.POST.get('val_sex')
        val_age = request.POST.get('val_age')
        val_adress = request.POST.get('val_adress')
        val_consultId = request.POST.get('val_consult')
        val_prc_possitive = request.POST.get('val_prc_possitive') == 'on'
        val_date_prc = request.POST.get('val_date_prc')
        # Update context
        context['person'].id = pk
        context['person'].ci = val_ci.strip()
        context['person'].name = val_name
        context['person'].last_names = val_last_names
        context['person'].sex = val_sex
        context['person'].age = val_age
        context['person'].address = val_adress
        context['person'].consulting_room_id = val_consultId
        context['person'].positive_pcr = val_prc_possitive
        context['person'].date_pcr = val_date_prc
        # Try execpt
        try:
            """ Validate CI """
            validateCI(str(val_ci).strip())
            # Validate pcr and date
            if val_prc_possitive and val_date_prc == '':
                raise Exception(getNoDatePcr())
            elif not val_prc_possitive and val_date_prc != '':
                raise Exception(getNoPcrSelect())
            # Update Person Values
            person.ci = val_ci.strip()
            person.name = val_name
            person.last_names = val_last_names
            person.sex = val_sex
            person.age = int(val_age)
            person.address = val_adress
            person.consulting_room = ConsultingRoom.objects.get(pk=int(val_consultId))
            person.positive_pcr = val_prc_possitive
            person.date_pcr = None if val_date_prc == '' else getDateFromString(val_date_prc)
            person.save()
            # Render to list after create
            messages.success(request, getSuccessEditMessage("Persona"))
            return redirect('peopleListView')
        except ValidationError:
            # Validate Unique CI
            messages.error(request, getUniqueCIError("Persona", val_ci))
        except Exception as e:
            # Manage All posible Errors
            messages.error(request, e.args[0])
    # Render Form
    return render(request, 'people/addOrEdit.html', context)


""" DELETE PERSON """


@login_required(login_url='/login')
@checkUserAccess(rol='SPECIALIST', error_url='/403')
def peopleDeleteView(request, pk):
    people = People.objects.get(id=pk)
    try:
        people.delete()
        messages.success(request, getDelSuccessText("Persona", people.name))
    except ProtectedError:
        messages.error(request, getDelProtectText("Persona", people.name))
    return redirect('peopleListView')


""" Export to Excel """

def peopleExportView(request):
    rows = [['CI', 'Nombre', 'Apellidos', "Sexo", "Edad", "Direccion", "Consultorio", "PCR Positivo"]]
    for person in People.objects.all():
        rows.append([
            person.ci,
            person.name,
            person.last_names,
            person.sex,
            person.age,
            person.address,
            person.consulting_room.name + " " + person.consulting_room.polyclinic.name,
            "SI" if person.positive_pcr is not None else "NO"
        ])
    sheet = excel.pe.Sheet(rows)
    return excel.make_response(sheet, "csv", file_name='listado de personas')