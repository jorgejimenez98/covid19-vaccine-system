from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.db.models import ProtectedError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.main.decorators import checkUserAccess
from apps.main.errorFunctions import *
from ..formClass import MunicipalityForm
from ..models import Municipality


""" Municipality LIST """


@login_required(login_url='/login')
@checkUserAccess(rol='ADMIN', error_url='/403')
def municipalityListView(request):
    # Init Context
    context = {"municipalities": Municipality.objects.all().order_by('-pk')}
    # Render List
    return render(request, 'municipality/list.html', context)
