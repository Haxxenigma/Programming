from django.urls import path
from rpg_app import views

urlpatterns = [
    path("", views.game),
]
