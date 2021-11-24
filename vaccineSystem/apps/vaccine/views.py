from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..main.decorators import checkUserAccess
from ..main.errorFunctions import *
from .models import Vaccine


""" VACCINE LIST """


@login_required(login_url='/login')
@checkUserAccess(rol='ADMIN', error_url='/403')
def vaccinesListView(request):
    # Init Context
    context = {"vaccines": Vaccine.objects.all().order_by('-pk')}
    # Render to vaccine List
    return render(request, 'vaccines/list.html', context)
