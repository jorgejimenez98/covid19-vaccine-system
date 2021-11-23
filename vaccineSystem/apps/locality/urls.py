from django.urls import path
from .views import municipalityViews as mviews
from .views import provinceViews as pviews
from .views import schoolViews as sviews
from .views import polyclinicViews as poviews
from .views import consultingRoomsViews as coviews

urlpatterns = [
    # Province urls
    path("provinces/list/", pviews.provinceListView, name='provinceListView'),
    path("provinces/add/", pviews.provinceAddView, name='provinceAddView'),
    path("provinces/edit/<int:pk>/", pviews.provinceEditView, name='provinceEditView'),
    path("provinces/delete/<int:pk>/", pviews.provinceDeleteView, name='provinceDeleteView'),
    # Municipality urls
    path("municipalities/list/", mviews.municipalityListView, name='municipalityListView'),
    path("municipalities/add/", mviews.municipalityAddView, name='municipalityAddView'),
    path("municipalities/edit/<int:pk>/", mviews.municipalityEditView, name='municipalityEditView'),
    path("municipalities/delete/<int:pk>/", mviews.municipalityDeleteView, name='municipalityDeleteView'),
    # School urls
    path("schools/list/", sviews.schoolListView, name='schoolListView'),
    path("schools/add/", sviews.schoolAddView, name='schoolAddView'),
    path("schools/edit/<int:pk>/", sviews.schoolEditView, name='schoolEditView'),
    path("schools/delete/<int:pk>/", sviews.schoolDeleteView, name='schoolDeleteView'),
    # Polyclinic urls
    path("polyclinics/list/", poviews.polyclinicListView, name='polyclinicListView'),
    path("polyclinics/add/", poviews.polyclinicAddView, name='polyclinicAddView'),
    path("polyclinics/edit/<int:pk>/", poviews.polyclinicEditView, name='polyclinicEditView'),
    path("polyclinics/delete/<int:pk>/", poviews.polyclinicDeleteView, name='polyclinicDeleteView'),
    # Consult Rooms Urls
    path("consults/list/", coviews.consultingRoomListView, name='consultingRoomListView')
]
