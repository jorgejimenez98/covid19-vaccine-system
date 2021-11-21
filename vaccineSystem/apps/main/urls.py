from django.urls import path
from . import views

urlpatterns = [
    path("", views.homeView, name="homeView"),
    path("login/", views.loginView, name="loginView"),
    path("logout/", views.logoutView, name="logoutView"),
    path("dashboard/", views.dashboardView, name="dashboardView"),
    path("403/", views.error404View, name="error404View"),
]
