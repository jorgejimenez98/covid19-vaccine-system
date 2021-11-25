from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.db.models import ProtectedError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..main.decorators import checkUserAccess
from ..main.errorFunctions import *
from .models import People


""" Consulting Room LIST """


@login_required(login_url='/login')
@checkUserAccess(rol='SPECIALIST', error_url='/403')
def peopleListView(request):
    # Init Context
    context = {"persons": People.objects.all()}
    # Render List
    return render(request, 'people/list.html', context)