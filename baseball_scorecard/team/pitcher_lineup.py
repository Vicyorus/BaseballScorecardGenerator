from baseball_scorecard.stats.pitcher_stats import PitcherStats
from baseball_scorecard.team.roster import Roster
from baseball_scorecard.team.player import Player


class PitcherLineup:
    def __init__(self, starting_pitcher_id: int, roster: Roster):
        # Get the starting pitcher.
        starting_pitcher = roster.get_player(starting_pitcher_id)

        # Set the object attributes.
        self.pitchers: list[Player] = [starting_pitcher]
        self.total_pitcher_stats: PitcherStats = None

        # Mark the starting pitcher as such.
        starting_pitcher.set_lineup_position("1", 1)

    def add_pitcher(self, pitcher: Player, inning_entered: int = 1):
        pitcher.set_lineup_position("1", inning_entered)
        self.pitchers.append(pitcher)

    def get_current_pitcher(self) -> Player:
        return self.pitchers[-1]

    def get_pitching_totals(self) -> PitcherStats:
        if not self.total_pitcher_stats:
            self.total_pitcher_stats = PitcherStats()
            for pitcher in self.pitchers:
                self.total_pitcher_stats.add_stats(pitcher.pitcher_stats)

        return self.total_pitcher_stats

    def get_pitcher_info_metapost_data(self) -> str:
        result = ""
        for idx, pitcher in enumerate(self.pitchers, start=1):
            result += pitcher.get_pitcher_metapost_data(idx)

        return result

    def get_pitcher_stats_metapost_data(self) -> str:
        result = ""

        for idx, pitcher in enumerate(self.pitchers, start=1):
            result += pitcher.pitcher_stats.get_metapost_data(idx)

        # Call the pitching totals function to ensure the totals are
        # properly set before printing them.
        self.get_pitching_totals()

        # Add the totals for all pitchers.
        result += self.total_pitcher_stats.get_metapost_data(13)

        return result

    def __str__(self):
        result = ""
        for pitcher in self.pitchers:
            result += pitcher.get_pitcher_str()

        return result
