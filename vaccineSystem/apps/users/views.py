from django.db import IntegrityError
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
    context = {"users": get_user_model().objects.all().order_by('-pk')}
    # Render List
    return render(request, 'users/list.html', context)


""" ADD USER """


@login_required(login_url='/login')
@checkUserAccess(rol='ADMIN', error_url='/403')
def userAddView(request):
    # Init Context
    context = {"user": UserForm(None, "", "", "", "", "")}
    # Render User Form
    if request.method == 'POST':
        # Get data from template
        name = request.POST.get("val_name")
        username = request.POST.get("val_username")
        rol = request.POST.get("val_rol")
        password = request.POST.get("val_password")
        confirmPassword = request.POST.get("val_confirm_password")
        # Update context
        context['user'].name = name
        context['user'].username = username
        context['user'].rol = rol
        context['user'].password = password
        context['user'].confirmPassword = confirmPassword
        try:
            # Create user
            get_user_model().objects.create_user(
                username=username,
                name=name,
                is_staff=True if rol == 'ADMIN' else False,
                isSpecialist=True if rol == 'SPECIALIST' else False,
                password=password
            )
            # Redirect User List
            messages.success(request, getSuccessCreatedMessage('Usuario'))
            return redirect("userListView")
        except IntegrityError:
            # Validate Unique username field
            messages.error(request, getUniqueUserError(username))
        except Exception as e:
            # Validate all posible errors
            messages.error(request, e.args[0])
    return render(request, 'users/add.html', context)


""" EDIT USER """


@login_required(login_url='/login')
@checkUserAccess(rol='ADMIN', error_url='/403')
def userEditView(request, pk):
    # Get User to Edit
    user = get_user_model().objects.get(pk=pk)
    userForm = UserForm(user.pk, user.name, user.username,"", "", "")
    userForm.rol = 'ADMIN' if user.is_staff else "SPECIALIST"
    # Init Context
    context = {"user": userForm}
    # Render User Form
    if request.method == 'POST':
        # Get data from template
        name = request.POST.get("val_name")
        username = request.POST.get("val_username")
        rol = request.POST.get("val_rol")
        # Update context
        context['user'].name = name
        context['user'].username = username
        context['user'].rol = rol
        try:
            # Validate if there is only an Admin user
            if user.is_staff and get_user_model().objects.filter(is_staff=True).count() == 1 and rol != 'ADMIN':
                raise Exception(getNoAdminDeleteMessage(user.username))
            # Edit user
            user.name = name
            user.username = str(username)
            user.is_staff = True if rol == 'ADMIN' else False
            user.isSpecialist = True if rol == 'SPECIALIST' else False
            user.save()
            # Redirect User List
            messages.success(request, getSuccessEditMessage('Usuario'))
            return redirect("userListView")
        except IntegrityError:
            # Validate Unique username field
            messages.error(request, getUniqueUserError(username))
        except Exception as e:
            # Validate all posible errors
            messages.error(request, e.args[0])
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
