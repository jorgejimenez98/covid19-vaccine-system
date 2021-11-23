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
