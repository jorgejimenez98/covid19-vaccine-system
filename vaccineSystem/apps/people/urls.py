from django.urls import path
from . import views

urlpatterns = [
    path('persons/list', views.peopleListView, name='peopleListView'),
    path('persons/add', views.peopleAddView, name='peopleAddView'),
]
