from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.db.models import ProtectedError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.main.decorators import checkUserAccess
from apps.main.errorFunctions import *
from ..formClass import ProvinceForm
from ..models import Province


""" PROVINCE LIST """


@login_required(login_url='/login')
@checkUserAccess(rol='ADMIN', error_url='/403')
def provinceListView(request):
    # Init Context
    context = {"provinces": Province.objects.all().order_by('-pk')}
    # Render List
    return render(request, 'province/list.html', context)


""" ADD PROVINCE """


@login_required(login_url='/login')
@checkUserAccess(rol='ADMIN', error_url='/403')
def provinceAddView(request):
    # Init Context
    context = {"province": ProvinceForm(None, "")}
    # Render Province Form
    if request.method == 'POST':
        # Get data from template
        name = request.POST.get("val_name")
        # Update context
        context['province'].name = name
        try:
            # Create user
            Province.objects.create(name=name)
            # Redirect User List
            messages.success(request, getSuccessCreatedMessage('Provincia'))
            return redirect("provinceListView")
        except IntegrityError:
            # Validate Unique username field
            messages.error(request, getUniqueTypeError('Provincia', name))
        except Exception as e:
            # Validate all posible errors
            messages.error(request, e.args[0])
    return render(request, 'province/add.html', context)


""" EDIT USER """


@login_required(login_url='/login')
@checkUserAccess(rol='ADMIN', error_url='/403')
def provinceEditView(request, pk):
    # Get Province to Edit
    province = Province.objects.get(pk=pk)
    provinceForm = ProvinceForm(province.pk, province.name)
    # Init Context
    context = {"province": provinceForm}
    # Render Province Form
    if request.method == 'POST':
        # Get data from template
        name = request.POST.get("val_name")
        # Update context
        context['province'].name = name
        try:
            # Edit user
            province.name = name
            province.save()
            # Redirect User List
            messages.success(request, getSuccessEditMessage('Provincia'))
            return redirect("provinceListView")
        except IntegrityError:
            # Validate Unique username field
            messages.error(request, getUniqueTypeError('Provincia', name))
        except Exception as e:
            # Validate all posible errors
            messages.error(request, e.args[0])
    return render(request, 'province/add.html', context)


""" DELETE PROVINCE """


@login_required(login_url='/login')
@checkUserAccess(rol='ADMIN', error_url='/403')
def provinceDeleteView(request, pk=None):
    # Get Province from database
    provinceToDelete = Province.objects.get(pk=pk)
    try:
        # Delete Province
        provinceToDelete.delete()
        # Send success message
        message = getDelSuccessText('Provincia', provinceToDelete.name)
        messages.success(request, message)
    except ProtectedError:
        # Send error Message
        message = getDelProtectText('Provincia', provinceToDelete.name)
        messages.error(request, message)
    # Render to province list after deletion
    return redirect('provinceListView')
