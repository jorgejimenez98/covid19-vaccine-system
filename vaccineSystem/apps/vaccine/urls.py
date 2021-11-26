from django.urls import path
from .views import vaccineViews as vviews
from .views import peopleVaccinations as pviews

urlpatterns = [
    path("vaccines/list", vviews.vaccinesListView, name="vaccinesListView"),
    path("vaccines/add", vviews.vaccinesAddView, name="vaccinesAddView"),
    path("vaccines/edit/<int:pk>", vviews.vaccinesEditView, name="vaccinesEditView"),
    path("vaccines/delete/<int:pk>/", vviews.vaccinesDeleteView, name="vaccinesDeleteView"),

    # People Vaccines Views
    path("person/vaccines/<int:pk>", pviews.personVaccinesList, name="personVaccinesList"),
]
