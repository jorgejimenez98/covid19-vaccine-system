from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.db.models import ProtectedError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.main.decorators import checkUserAccess
from apps.main.errorFunctions import *
from ..formClass import SchoolForm
from ..models import ConsultingRoom, Polyclinic


""" Consulting Room LIST """


@login_required(login_url='/login')
@checkUserAccess(rol='ADMIN', error_url='/403')
def consultingRoomListView(request):
    # Init Context
    context = {"consults": ConsultingRoom.objects.all().order_by('-pk')}
    # Render List
    return render(request, 'consults/list.html', context)


""" ADD CONSULT ROOM """


@login_required(login_url='/login')
@checkUserAccess(rol='ADMIN', error_url='/403')
def consultRoomAddView(request):
    # Init Context
    context = {
        "con": SchoolForm(None, "", "", ""),
        "pols": Polyclinic.objects.all().order_by('-pk')
    }
    # Render Pol Form
    if request.method == 'POST':
        # Get data from template
        name = request.POST.get("val_name")
        val_pol_id = request.POST.get("val_pol_id")
        # Update context
        context['con'].name = name
        context['con'].munId = val_pol_id
        try:
            # Create
            ConsultingRoom.objects.create(
                name=name,
                polyclinic=Polyclinic.objects.get(pk=int(val_pol_id))
            )
            # Redirect List
            messages.success(request, getSuccessCreatedMessage('Consultorio'))
            return redirect("consultingRoomListView")
        except Exception as e:
            # Validate all posible errors
            messages.error(request, e.args[0])
    return render(request, 'consults/addOrEdit.html', context)


""" ADD CONSULT ROOM """


@login_required(login_url='/login')
@checkUserAccess(rol='ADMIN', error_url='/403')
def consultRoomEditView(request, pk):
    con = ConsultingRoom.objects.get(pk=pk)
    # Init Context
    context = {
        "con": SchoolForm(con.id, con.name, con.polyclinic.pk, con.polyclinic.name),
        "pols": Polyclinic.objects.all().order_by('-pk')
    }
    # Render Pol Form
    if request.method == 'POST':
        # Get data from template
        name = request.POST.get("val_name")
        val_pol_id = request.POST.get("val_pol_id")
        # Update context
        context['con'].name = name
        context['con'].munId = val_pol_id
        try:
            # Update
            con.name = name
            con.polyclinic = Polyclinic.objects.get(pk=int(val_pol_id))
            con.save()
            # Redirect List
            messages.success(request, getSuccessEditMessage('Consultorio'))
            return redirect("consultingRoomListView")
        except Exception as e:
            # Validate all posible errors
            messages.error(request, e.args[0])
    return render(request, 'consults/addOrEdit.html', context)


""" DELETE CONSULT ROOM  """


@login_required(login_url='/login')
@checkUserAccess(rol='ADMIN', error_url='/403')
def consultRoomDeleteView(request, pk):
    # Get Data from template
    consultingRoom = ConsultingRoom.objects.get(pk=pk)
    try:
        # Delete Pol
        consultingRoom.delete()
        # Redirect Pol List
        message = getDelSuccessText('Consultorio', consultingRoom.name)
        messages.success(request, message)
    except ProtectedError:
        # Send error Message
        message = getDelProtectText('Consultorio', consultingRoom.name)
        messages.error(request, message)
    return redirect("consultingRoomListView")
