from django.urls import path
from . import views

urlpatterns = [
    path('persons/list', views.peopleListView, name='peopleListView'),
    path('persons/add', views.peopleAddView, name='peopleAddView'),
    path('persons/export', views.peopleExportView, name='peopleExportView'),
    path('persons/delete/<int:pk>/', views.peopleDeleteView, name='peopleDeleteView'),
    path('persons/edit/<int:pk>/', views.peopleEditView, name='peopleEditView'),
]
