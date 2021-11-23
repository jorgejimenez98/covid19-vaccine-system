from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.db.models import ProtectedError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.main.decorators import checkUserAccess
from apps.main.errorFunctions import *
from ..formClass import SchoolForm
from ..models import Municipality, School


""" SCHOOLS LIST """


@login_required(login_url='/login')
@checkUserAccess(rol='ADMIN', error_url='/403')
def schoolListView(request):
    # Init Context
    context = {"schools": School.objects.all().order_by('-pk')}
    # Render List
    return render(request, 'school/list.html', context)


""" ADD SCHOOLS """


@login_required(login_url='/login')
@checkUserAccess(rol='ADMIN', error_url='/403')
def schoolAddView(request):
    # Init Context
    context = {
        "school": SchoolForm(None, "", "", ""),
        "muns": Municipality.objects.all().order_by('-pk')
    }
    # Render Mun Form
    if request.method == 'POST':
        # Get data from template
        name = request.POST.get("val_name")
        val_mun_id = request.POST.get("val_mun_id")
        # Update context
        context['school'].name = name
        context['school'].munId = val_mun_id
        try:
            # Create Schools
            School.objects.create(
                name=name,
                municipality=Municipality.objects.get(pk=int(val_mun_id))
            )
            # Redirect MUN List
            messages.success(request, getSuccessCreatedMessage('Escuela'))
            return redirect("schoolListView")
        except Exception as e:
            # Validate all posible errors
            messages.error(request, e.args[0])
    return render(request, 'school/addOrdEdit.html', context)


""" EDIT SCHOOLS """


@login_required(login_url='/login')
@checkUserAccess(rol='ADMIN', error_url='/403')
def schoolEditView(request, pk):
    # Get Data from template
    school = School.objects.get(pk=pk)
    # Init Context
    context = {
        "school": SchoolForm(school.pk, school.name, school.municipality.pk, school.municipality.name),
        "muns": Municipality.objects.all().order_by('-pk')
    }
    # Render Mun Form
    if request.method == 'POST':
        # Get data from template
        name = request.POST.get("val_name")
        val_mun_id = request.POST.get("val_mun_id")
        # Update context
        context['school'].name = name
        context['school'].munId = val_mun_id
        try:
            # Update Schools
            school.name = name
            school.municipality = Municipality.objects.get(pk=int(val_mun_id))
            school.save()
            # Redirect MUN List
            messages.success(request, getSuccessEditMessage('Escuela'))
            return redirect("schoolListView")
        except Exception as e:
            # Validate all posible errors
            messages.error(request, e.args[0])
    return render(request, 'school/addOrdEdit.html', context)


""" DELETE SCHOOLS """


@login_required(login_url='/login')
@checkUserAccess(rol='ADMIN', error_url='/403')
def schoolDeleteView(request, pk):
    # Get School from template
    school = School.objects.get(pk=pk)
    try:
        # Delete Mun
        school.delete()
        # Redirect MUN List
        message = getDelSuccessText('Escuela', school.name)
        messages.success(request, message)
    except ProtectedError:
        # Send error Message
        message = getDelProtectText('Escuela', school.name)
        messages.error(request, message)
    return redirect("schoolListView")
