from django.urls import path
from .views import *

urlpatterns = [
    path('combatants', get_combatants)
]