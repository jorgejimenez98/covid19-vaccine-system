from django.urls import path
from . import views

urlpatterns = [
    path("users/list/", views.userListView, name="userListView"),
    path("users/delete/<int:pk>/", views.userDeleteView, name="userDeleteView")
]
