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
    path("person/vaccines/delete/<int:pk>/<str:vaccine>/<str:vaccineId>/", pviews.personVaccinesDelete, name="personVaccinesDelete"),
    path("person/vaccines/add/school/<int:pk>", pviews.personAddSchoolVaccine, name="personAddSchoolVaccine"),
    path("person/vaccines/add/consult/<int:pk>", pviews.personAddConsultVaccine, name="personAddConsultVaccine"),
    path("person/vaccines/add/health/<int:pk>", pviews.personAddHealthVaccine, name="personAddHealthVaccine"),
]
