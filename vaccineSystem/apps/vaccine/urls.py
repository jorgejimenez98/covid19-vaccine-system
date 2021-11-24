from django.urls import path
from . import views


urlpatterns = [
    path("vaccines/list", views.vaccinesListView, name="vaccinesListView"),
]
