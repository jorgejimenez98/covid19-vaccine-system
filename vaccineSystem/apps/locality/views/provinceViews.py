from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.main.decorators import checkUserAccess
from apps.main.errorFunctions import *
from ..formClass import ProvinceForm, MunicipalityForm
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
