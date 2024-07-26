from scorecard.at_bat import AtBat

class Inning:
    def __init__(self, number, top, away_team, home_team):
        self.number = number
        self.top = top
        self.plays = []
        self.current_ab = None
        self.outs = {1: False, 2: False, 3: False}

        if self.top:
            self.fielding_team = home_team
            self.batting_team = away_team
        else:
            self.fielding_team = away_team
            self.batting_team = home_team

    def new_ab(self):
        ab = AtBat(self.batting_team.get_batter(), self.fielding_team.get_pitcher())
        self.batting_team.next_batter()
        self.plays.append(ab)
        self.current_ab = ab

    def pitching_substitution(self, pitcher_id):
        self.fielding_team.add_pitcher(pitcher_id, self.number)

    def offensive_substitution(self, order, player_id, position):
        self.batting_team.add_player(order, player_id, position, self.number)

    def defensive_substitution(self, order, player_id, position):
        self.fielding_team.add_player(order, player_id, position, self.number)

    def pitch_list(self, pitches):
        self.current_ab.pitch_list(pitches)

    def out(self, play):
        # Sanity check, ensure the user isn't adding more than 3 outs.
        out_added = False
        for i in range(1, 4):
            if not self.outs[i]:
                self.outs[i] = True
                out_added = True
                break
        if not out_added:
            raise Exception("More than 3 outs in inning")

        # Add double and triple play stats to the batter team.
        if "DP" in play:
            self.batting_team.get_stats().double_plays += 1
        if "TP" in play:
            self.batting_team.get_stats().triple_plays += 1

        self.current_ab.out(play)

    def advance(self, end_base, play):
        return None

    def thrown_out(self, out_base, play, out_number, pitcher_id):
        return None

    def hit(self, bases):
        return None

    def reach(self, play, end_base=None):
        return None

    def error(self, fielder):
        return None

    def atbase(self, label):
        return None

    def no_ab(self, label):
        return None

    def __str__(self):
        inn = "Top" if self.top else "Bottom"
        result = f"{inn} of the {self.__ordinal(self.number)}\n"
        for ab in self.plays:
            result += f'{ab}'

        result += "\n"
        return result

    def __ordinal(self, n):
        if 11 <= (n % 100) <= 13:
            suffix = 'th'
        else:
            suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
        return str(n) + suffix
