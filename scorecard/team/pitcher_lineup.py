from scorecard.stats.pitcher_stats import PitcherStats

class PitcherLineup:
    def __init__(self, starting_pitcher, roster):
        self.pitchers = [starting_pitcher]
        self.roster = roster
        self.roster.get_player(starting_pitcher).set_lineup_position("1", 1)

        self.total_pitcher_stats = None

    def add_pitcher(self, player_id):
        self.pitchers.append(player_id)

    def get_pitcher(self):
        pitcher_id = self.pitchers[-1]
        return self.roster.get_player(pitcher_id)

    def is_in_lineup(self, pitcher_id):
        for id in self.pitchers:
            if id == pitcher_id:
                return True

        return False

    def get_pitching_totals(self):
        if not self.total_pitcher_stats:
            self.total_pitcher_stats = PitcherStats()
            for pitcher_id in self.pitchers:
                pitcher = self.roster.get_player(pitcher_id)
                self.total_pitcher_stats.add_stats(pitcher.pitcher_stats)

        return self.total_pitcher_stats

    def get_pitcher_info_metapost_data(self):
        result = ""
        for idx, pitcher_id in enumerate(self.pitchers, start=1):
            pitcher = self.roster.get_player(pitcher_id)
            result += pitcher.get_pitcher_metapost_data(idx)

        return result

    def get_pitcher_stats_metapost_data(self):
        result = ""

        for idx, pitcher_id in enumerate(self.pitchers, start=1):
            pitcher = self.roster.get_player(pitcher_id)
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
            result += f'{str(self.roster.get_player(pitcher).get_pitcher_str())}\n'

        return result
