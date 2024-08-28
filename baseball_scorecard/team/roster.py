from baseball_scorecard.team.player import Player

class Roster:
    def __init__(self, roster, lefties, use_extended_roster):

        self.players = {}

        for player_id, player_data in roster.items():
            is_lefty = False
            if player_id in lefties:
                is_lefty = True

            if use_extended_roster:
                player = Player(player_id, player_data["jersey"], player_data["name"], is_lefty)
            else:
                player = Player(player_id, player_id, player_data, is_lefty)

            self.players[player_id] = player

    def get_player(self, id):
        if id in self.players.keys():
            return self.players[id]

        return None

    def __str__(self):
        result = ""
        for player_id in self.players.keys():
            result += f'{str(self.players[player_id])}\n'

        return result
