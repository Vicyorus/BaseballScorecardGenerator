from baseball_scorecard.team.player import Player


class Roster:
    def __init__(
        self,
        roster: dict[int, str | dict[str, int | str]],
        lefties: list[int],
        use_extended_roster: bool = False,
    ):

        self.players: dict[int, Player] = {}

        for player_id, player_data in roster.items():
            is_lefty = True if player_id in lefties else False

            if use_extended_roster:
                player = Player(
                    player_id, player_data["jersey"], player_data["name"], is_lefty
                )
            else:
                player = Player(player_id, player_id, player_data, is_lefty)

            self.players[player_id] = player

    def get_player(self, id: int) -> Player:
        try:
            return self.players[id]
        except KeyError:
            raise Exception(f"Player with ID {id} was not found")

    def __str__(self):
        result = ""
        for player_id in self.players.keys():
            result += f"{str(self.players[player_id])}\n"

        return result
