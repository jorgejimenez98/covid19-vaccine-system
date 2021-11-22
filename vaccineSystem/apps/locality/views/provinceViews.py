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
