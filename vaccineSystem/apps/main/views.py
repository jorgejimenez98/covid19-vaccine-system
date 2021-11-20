from django.shortcuts import render, redirect


def homeView(request):
    context = {}
    if not request.user.is_authenticated:
        return redirect('loginView')
    return redirect('dashboardView')


def loginView(request):
    context = {}
    return render(request, 'login.html', context)


def dashboardView(request):
    context = {}
    return render(request, 'home.html', context)
