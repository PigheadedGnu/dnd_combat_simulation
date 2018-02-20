from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .src.managers.combatant_manager import CombatantManager
from .src.battle_runner import BattleRunner
from .src.managers.action_manager import ActionManager
from .src.managers.effect_manager import EffectManager


def error_response(status, msg):
    response = JsonResponse({'msg': msg})
    response.status_code = status
    return response


def get_combatants(request):
    manager = CombatantManager()
    return JsonResponse(manager.get_all_combatants(), safe=False)


def get_simulation_result(request):
    br = BattleRunner()
    team1 = request.POST.get("team1")
    team2 = request.POST.get("team2")
    if team1 == "" or team2 == "":
        return error_response(400, "Both teams must have at least 1 combatant!")
    br.run_simulator(team1.split(","),
                     team2.split(","),
                     200)
    return JsonResponse(br.get_results().to_json(), safe=False)