from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..main.decorators import checkUserAccess
from ..main.errorFunctions import *
from .formclass import UserForm


""" USERS LIST """
@login_required(login_url='/login')
@checkUserAccess(rol='ADMIN', error_url='/403')
def userListView(request):
    context = {"users": get_user_model().objects.all()}
    return render(request, 'users/list.html', context)



@login_required(login_url='/login')
@checkUserAccess(rol='ADMIN', error_url='/403')
def userAddView(request):
    context = {"user": UserForm("", "", "", "", "")}
    return render(request, 'users/add.html', context)


@login_required(login_url='/login')
@checkUserAccess(rol='ADMIN', error_url='/403')
def userDeleteView(request, pk=None):
    user = get_user_model().objects.get(pk=pk)
    if user.is_staff and get_user_model().objects.filter(is_staff=True).count() == 1:
        messages.error(request, getNoAdminDeleteMessage(user.username))
    else:
        user.delete()
        messages.error(request, deleteSuccessMessage(user.username))
    return redirect("userListView")
