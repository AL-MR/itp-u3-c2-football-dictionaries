from football_dictionaries.assignment_1 import players_as_dictionaries


def players_by_country_and_position(squads_list):
    players = players_as_dictionaries(squads_list)
    result = {}
    for player in players:
        result.setdefault(player['country'], {})
        result[player['country']].setdefault(player['position'], [])
        result[player['country']][player['position']].append(player)
    return result