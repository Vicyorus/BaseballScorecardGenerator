class PitcherLineup:
    def __init__(self, starting_pitcher, roster):
        self.pitchers = [starting_pitcher]
        self.roster = roster # TODO: May want to remove this when the debugging stage is done
        self.roster.get_player(starting_pitcher).set_lineup_position("1", 1)

    def add_pitcher(self, player_id):
        self.pitchers.append(player_id)

    def get_pitcher(self):
        pitcher_id = self.pitchers[-1]
        return self.roster.get_player(pitcher_id)

    def __str__(self):
        result = ""
        for pitcher in self.pitchers:
            result += f'{str(self.roster.get_player(pitcher))}\n'

        return result

