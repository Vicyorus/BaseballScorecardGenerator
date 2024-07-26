class Reserves:
    def __init__(self, bullpen_data, bench_data, roster):
        self.bullpen = []
        self.bench = []
        self.roster = roster

        for player_id in bullpen_data:
            self.roster.get_player(player_id).set_as_bullpen()
            self.bullpen.append(player_id)

        for player in bench_data:
            self.roster.get_player(player[0]).set_primary_position(player[1])
            self.bench.append(player[0])

    def __str__(self):
        result = ""

        for player_id in self.bench:
            player = self.roster.get_player(player_id)
            if player.is_in_lineup():
                result += f'~~{str(player.get_reserves_str())}~~\n'
            else:
                result += f'{str(player.get_reserves_str())}\n'

        result += "\n"

        for pitcher_id in self.bullpen:
            pitcher = self.roster.get_player(pitcher_id)
            if pitcher.is_in_lineup():
                result += f'~~{str(self.roster.get_player(pitcher_id).get_reserves_str())}~~\n'
            else:
                result += f'{str(self.roster.get_player(pitcher_id).get_reserves_str())}\n'

        return result

