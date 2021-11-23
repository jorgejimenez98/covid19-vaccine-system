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