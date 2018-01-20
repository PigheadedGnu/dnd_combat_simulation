from django.shortcuts import render
from django.http import JsonResponse
from .src.managers.combatant_manager import CombatantManager
from .src.managers.action_manager import ActionManager
from .src.managers.effect_manager import EffectManager


def get_combatants(request):
    manager = CombatantManager()
    return JsonResponse(manager.get_all_combatants(), safe=False)
