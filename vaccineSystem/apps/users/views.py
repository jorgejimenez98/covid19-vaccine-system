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
    # Init Context
    context = {"users": get_user_model().objects.all()}
    # Render List
    return render(request, 'users/list.html', context)


""" ADD USER """
@login_required(login_url='/login')
@checkUserAccess(rol='ADMIN', error_url='/403')
def userAddView(request):
    # Init Context
    context = {"user": UserForm("", "", "", "", "")}
    # Render User Form
    if request.method == 'POST':
        print('AAA', request.POST)
    return render(request, 'users/add.html', context)


""" DELETE USER """
@login_required(login_url='/login')
@checkUserAccess(rol='ADMIN', error_url='/403')
def userDeleteView(request, pk=None):
    # Get user data from template
    user = get_user_model().objects.get(pk=pk)
    # Validate if there is onle an Admin user
    if user.is_staff and get_user_model().objects.filter(is_staff=True).count() == 1:
        messages.error(request, getNoAdminDeleteMessage(user.username))
    else:
        # Delete user after validation
        user.delete()
        messages.error(request, deleteSuccessMessage(user.username))
    # Render to users list
    return redirect("userListView")
