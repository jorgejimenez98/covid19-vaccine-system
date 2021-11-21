from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from ..main.decorators import checkUserAccess


@login_required(login_url='/login')
@checkUserAccess(rol='ADMIN', error_url='/403')
def userListView(request):
    context = {"users": get_user_model().objects.all()}
    return render(request, 'users/list.html', context)
