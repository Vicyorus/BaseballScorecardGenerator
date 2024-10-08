from baseball_scorecard.plays.substitution.fielder import DefensiveSubstitution
from baseball_scorecard.stats.pitcher_stats import PitcherStats
from baseball_scorecard.stats.team_stats import TeamStats
from baseball_scorecard.team.lineup import Lineup
from baseball_scorecard.team.pitcher_lineup import PitcherLineup
from baseball_scorecard.team.player import Player
from baseball_scorecard.team.reserves import Reserves
from baseball_scorecard.team.roster import Roster


class Team:

    team_name_template = (
        "    label.top(btex {{\\bigsf {}}} etex rotated 90, game_team) withcolor clr;\n"
    )

    def __init__(
        self,
        data: dict[
            str,
            str
            | int
            | list[int]
            | list[list[int, str]]
            | dict[int, str | dict[str, int | str]],
        ],
        use_extended_roster: bool = False,
        is_away_team: bool = False,
    ):
        self.team: str = data["team"]
        self.is_away_team: bool = is_away_team

        self.roster: Roster = Roster(
            data["roster"], data["lefties"], use_extended_roster
        )
        self.lineup: Lineup = Lineup(data["lineup"], self.roster)
        self.pitcher_lineup: PitcherLineup = PitcherLineup(data["starter"], self.roster)
        self.reserves: Reserves = Reserves(data["bullpen"], data["bench"], self.roster)
        self.stats: TeamStats = TeamStats()

        self.defensive_subs: dict[int, list[DefensiveSubstitution]] = {}

    def add_pitcher(self, pitcher_id: int, inning: int):
        pitcher = self.roster.get_player(pitcher_id)
        self.pitcher_lineup.add_pitcher(pitcher, inning)

    def add_player(
        self,
        order: int,
        player_id: int,
        position: str,
        inning: int,
        is_defensive_sub: bool = False,
    ):
        player = self.roster.get_player(player_id)
        self.lineup.add_player(order, player, position, inning)

        # For defensive substitutions, register the event on the team,
        # to be later handled when the inning either prints the data, or
        # generates the baseball_scorecard.
        if is_defensive_sub:
            if inning in self.defensive_subs.keys():
                self.defensive_subs[inning].append(
                    DefensiveSubstitution(order, str(player), self.is_away_team)
                )
            else:
                self.defensive_subs[inning] = [
                    DefensiveSubstitution(order, str(player), self.is_away_team)
                ]

    def defensive_switch(self, player_id: int, position: str):
        player = self.roster.get_player(player_id)
        player.add_defensive_position(position)

    def next_batter(self):
        return self.lineup.next_batter()

    def no_ab(self):
        self.lineup.no_ab()

    def winning_pitcher(self, pitcher_id: int):
        pitcher = self.roster.get_player(pitcher_id)
        pitcher.add_decision("W")

    def losing_pitcher(self, pitcher_id: int):
        pitcher = self.roster.get_player(pitcher_id)
        pitcher.add_decision("L")

    def save_pitcher(self, pitcher_id: int):
        pitcher = self.roster.get_player(pitcher_id)
        pitcher.add_decision("S")

    def get_player_in_lineup(self, player_id: int) -> tuple[int, Player]:
        lineup_pos, runner = self.lineup.get_player_in_lineup(player_id)

        if lineup_pos == -1:
            raise Exception(
                f"No player found with the ID {player_id} for team {self.team}"
            )

        return lineup_pos, runner

    def get_batter(self) -> Player:
        return self.lineup.get_batter()

    def get_previous_batter(self) -> tuple[int, Player]:
        return self.lineup.get_previous_batter()

    def get_current_pitcher(self) -> Player:
        return self.pitcher_lineup.get_current_pitcher()

    def get_stats(self) -> TeamStats:
        return self.stats

    def get_pitching_totals(self) -> PitcherStats:
        return self.pitcher_lineup.get_pitching_totals()

    def get_total_at_bats(self) -> int:
        return self.lineup.get_total_at_bats()

    def get_team_metapost_data(self) -> str:
        result = "    % team info\n"
        result += Team.team_name_template.format(self.team)
        result += "\n"
        result += self.lineup.get_batter_info_metapost_data()
        result += "\n"
        result += self.reserves.get_bench_metapost_data()
        return result

    def get_pitcher_metapost_data(self) -> str:
        result = "    % pitcher info\n"
        result += self.pitcher_lineup.get_pitcher_info_metapost_data()
        result += "\n"
        result += self.reserves.get_bullpen_metapost_data()
        return result

    def get_batter_stats_metapost_data(self) -> str:
        result = "    % batter stats\n"
        result += self.lineup.get_batter_stats_metapost_data()
        result += "\n"
        return result

    def get_pitcher_stats_metapost_data(self) -> str:
        result = "    % pitcher stats\n"
        result += self.pitcher_lineup.get_pitcher_stats_metapost_data()
        result += "\n"
        return result

    def get_stats_metapost_data(
        self, total_at_bats: int, pitching_stats: PitcherStats
    ) -> str:
        result = "    % team stats info\n"
        result = self.stats.get_metapost_data(total_at_bats, pitching_stats)
        return result

    def __str__(self):
        result = f"{self.team}\n\n"
        result += f"{str(self.lineup)}\n"
        result += f"{str(self.pitcher_lineup)}\n"
        result += f"{str(self.reserves)}\n"
        result += f"{str(self.stats)}\n"
        result += "\n"
        return result
