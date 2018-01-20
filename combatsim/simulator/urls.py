from django.urls import path, include
from simulator import views

urlpatterns = [
    path('/combatants', views.get_combatants)
]