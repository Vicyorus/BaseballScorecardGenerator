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

    def get_bench_metapost_data(self):
        result = "    % bench info\n"

        for idx, player_id in enumerate(self.bench, start=1):
            player = self.roster.get_player(player_id)
            result += player.get_bench_metapost_data(idx)

        return result

    def get_bullpen_metapost_data(self):
        result = "    % bullpen info\n"

        for idx, player_id in enumerate(self.bullpen, start=1):
            player = self.roster.get_player(player_id)
            result += player.get_bullpen_metapost_data(idx)

        return result

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

