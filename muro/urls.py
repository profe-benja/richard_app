
from django.urls import path
from muro import views

urlpatterns = [
    path("", views.index, name="muro_index"),
    path("create", views.create, name="muro_create"),
    path("<int:id>", views.show, name="muro_show"),
    path("<int:id>/edit", views.edit, name="muro_edit"),
    # path("", views.index, name="muro_index")
]
