from django.urls import path
from .views import *

urlpatterns = [
    path('combatants', get_combatants),
    path('simulate', get_simulation_result),
    path('actions', get_all_actions),
    path('createCombatant', create_combatant)
]