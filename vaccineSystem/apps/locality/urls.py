from django.urls import path
from .views import municipalityViews as mviews
from .views import provinceViews as pviews

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
]
