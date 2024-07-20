from at_bat import AtBat

class Inning:
    def __init__(self, number, top, away_team, home_team):
        self.number = number
        self.top = top
        self.plays = []

        if self.top:
            self.fielding_team = home_team
            self.batting_team = away_team
        else:
            self.fielding_team = away_team
            self.batting_team = home_team

    def new_ab(self):
        ab = AtBat()
        self.plays.append(ab)
        return ab

    def pitching_substitution(self, pitcher_id):
        self.fielding_team.add_pitcher(pitcher_id, self.number)
    
    def offensive_substitution(self, order, player_id, position):
        self.batting_team.add_player(order, player_id, position, self.number)

    def defensive_substitution(self, order, player_id, position):
        self.fielding_team.add_player(order, player_id, position, self.number)

    def __str__(self):
        inn = "Top" if self.top else "Bottom"
        return f"{inn} of the {self.__ordinal(self.number)}\n"

    def __ordinal(self, n):
        if 11 <= (n % 100) <= 13:
            suffix = 'th'
        else:
            suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
        return str(n) + suffix
