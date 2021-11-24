from django.urls import path
from . import views


urlpatterns = [
    path("vaccines/list", views.vaccinesListView, name="vaccinesListView"),
    path("vaccines/add", views.vaccinesAddView, name="vaccinesAddView"),
    path("vaccines/edit/<int:pk>", views.vaccinesEditView, name="vaccinesEditView"),
]
