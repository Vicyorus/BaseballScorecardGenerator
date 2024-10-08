from baseball_scorecard.team.roster import Roster
from baseball_scorecard.team.player import Player


class Reserves:
    def __init__(
        self, bullpen_data: list[int], bench_data: list[list[int | str]], roster: Roster
    ):
        self.bullpen: list[Player] = []
        self.bench: list[Player] = []

        for pitcher_id in bullpen_data:
            player = roster.get_player(pitcher_id)
            player.set_as_bullpen()
            self.bullpen.append(player)

        for bench_info in bench_data:
            player = roster.get_player(bench_info[0])
            player.set_primary_position(bench_info[1])
            self.bench.append(player)

    def get_bench_metapost_data(self) -> str:
        result = "    % bench info\n"

        for idx, player in enumerate(self.bench, start=1):
            result += player.get_bench_metapost_data(idx)

        return result

    def get_bullpen_metapost_data(self) -> str:
        result = "    % bullpen info\n"

        for idx, player in enumerate(self.bullpen, start=1):
            result += player.get_bullpen_metapost_data(idx)

        return result

    def __str__(self):
        result = ""

        for player in self.bench:
            result += player.get_reserves_str()

        result += "\n"

        for pitcher in self.bullpen:
            result += pitcher.get_reserves_str()

        return result
