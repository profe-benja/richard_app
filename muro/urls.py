
from django.urls import path
from muro import views

urlpatterns = [
    path("", views.index, name="muro_index"),
    path("create", views.create, name="muro_create"),
    # path("", views.index, name="muro_index")
]
