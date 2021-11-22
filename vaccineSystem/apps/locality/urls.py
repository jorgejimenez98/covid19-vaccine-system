from django.urls import path
from .views import municipalityViews as mviews
from .views import provinceViews as pviews

urlpatterns = [
    # Province urls
    path("provinces/list/", pviews.provinceListView, name='provinceListView'),
    path("provinces/add/", pviews.provinceAddView, name='provinceAddView'),
    path("provinces/edit/<int:pk>/", pviews.provinceEditView, name='provinceEditView'),
    path("provinces/delete/<int:pk>/", pviews.provinceDeleteView, name='provinceDeleteView'),
]
