from django.http import JsonResponse
from simulator.src.managers.combatant_manager import CombatantManager
from simulator.src.battle_runner import BattleRunner
from simulator.src.managers.action_manager import ActionManager


def error_response(status, msg):
    response = JsonResponse({'msg': msg})
    response.status_code = status
    return response


def get_combatants(request):
    manager = CombatantManager()
    return JsonResponse(manager.get_all_combatants(), safe=False)


def get_all_actions(request):
    manager = ActionManager()
    return JsonResponse(manager.get_all_actions(), safe=False)


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


def create_combatant(request):
    cm = CombatantManager()
    combatant_name = request.POST.get("name")
    hp = request.POST.get("hp")
    ac = request.POST.get("ac")
    proficiency = request.POST.get("proficiency")
    saves = {"STR": request.POST.get("strength"),
             "CON": request.POST.get("constitution"),
             "DEX": request.POST.get("dexterity"),
             "WIS": request.POST.get("wisdom"),
             "INT": request.POST.get("intelligence"),
             "CHA": request.POST.get("charisma")}
    actions = request.POST.get("actions").split(",")
    success, msg = cm.create_combatant(
        combatant_name, hp, ac, proficiency, saves, actions)

    if success:
        return JsonResponse(cm.get_all_combatants(reload=True), safe=False)
    else:
        return error_response(400, msg)





