from scorecard.team.player import Player
from scorecard.team.roster import Roster
from scorecard.team.lineup import Lineup
from scorecard.team.pitcher_lineup import PitcherLineup
from scorecard.team.reserves import Reserves
from scorecard.stats.team_stats import TeamStats

class Team:

    team_name_location = (2128,96)
    team_name_template = "    label.top(btex {{\\bigsf {}}} etex rotated 90, {}) withcolor clr;\n"

    def __init__(self, data, use_extended_roster):
        self.team = data["team"]
        self.lefties = data["lefties"]
        self.bench = data["bench"]
        self.bullpen = data["bullpen"]

        self.roster = Roster(data["roster"], use_extended_roster)
        self.lineup = Lineup(data["lineup"], self.roster)
        self.pitcher_lineup = PitcherLineup(data["starter"], self.roster)
        self.reserves = Reserves(data["bullpen"], data["bench"], self.roster)
        self.stats = TeamStats()

    def add_pitcher(self, pitcher_id, inning):
        # Sanity check, ensure the pitcher is in the roster.
        pitcher = self.roster.get_player(pitcher_id)
        if not pitcher:
            raise Exception(f'No pitcher found with the ID {pitcher_id} for team {self.team}')

        pitcher.set_lineup_position("1", inning)
        self.pitcher_lineup.add_pitcher(pitcher_id)

    def add_player(self, order, player_id, position, inning):
        # Sanity check, ensure the player is in the roster.
        player = self.roster.get_player(player_id)
        if not player:
            raise Exception(f'No player found with the ID {player_id} for team {self.team}')

        player.set_lineup_position(position, inning)

        self.lineup.add_player(order, player_id)

    def next_batter(self):
        return self.lineup.next_batter()

    def no_ab(self):
        self.lineup.no_ab()

    def get_batter(self):
        return self.lineup.get_batter()

    def get_pitcher(self):
        return self.pitcher_lineup.get_pitcher()

    def get_stats(self):
        return self.stats

    def get_pitching_totals(self):
        return self.pitcher_lineup.get_pitching_totals()

    def get_total_at_bats(self):
        return self.lineup.get_total_at_bats()

    def get_team_metapost_data(self):
        result = "    % team info\n"
        result += Team.team_name_template.format(self.team, Team.team_name_location)
        result += "\n"
        result += self.lineup.get_batter_info_metapost_data()
        result += "\n"
        result += self.reserves.get_bench_metapost_data()
        return result

    def get_pitcher_metapost_data(self):
        result = "    % pitcher info\n"
        result += self.pitcher_lineup.get_pitcher_info_metapost_data()
        result += "\n"
        result += self.reserves.get_bullpen_metapost_data()
        return result

    def get_batter_stats_metapost_data(self):
        result = "    % batter stats\n"
        result += self.lineup.get_batter_stats_metapost_data()
        result += "\n"
        return result

    def get_pitcher_stats_metapost_data(self):
        result = "    % pitcher stats\n"
        result += self.pitcher_lineup.get_pitcher_stats_metapost_data()
        result += "\n"
        return result

    def get_stats_metapost_data(self, total_at_bats, pitching_stats):
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
