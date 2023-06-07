
from django.urls import path
from muro import views

urlpatterns = [
    path("", views.index, name="muro_index"),
    # path("", views.index, name="muro_index")
]
