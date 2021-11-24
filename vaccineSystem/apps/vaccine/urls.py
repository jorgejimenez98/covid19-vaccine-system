from django.urls import path
from .views import vaccineViews


urlpatterns = [
    path("vaccines/list", vaccineViews.vaccinesListView, name="vaccinesListView"),
    path("vaccines/add", vaccineViews.vaccinesAddView, name="vaccinesAddView"),
    path("vaccines/edit/<int:pk>", vaccineViews.vaccinesEditView, name="vaccinesEditView"),
    path("vaccines/delete/<int:pk>/", vaccineViews.vaccinesDeleteView, name="vaccinesDeleteView"),
]
