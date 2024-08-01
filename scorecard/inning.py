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

    # Substitutions.
    def pitching_substitution(self, pitcher_id):
        self.fielding_team.add_pitcher(pitcher_id, self.number)

    def offensive_substitution(self, order, player_id, position):
        self.batting_team.add_player(order, player_id, position, self.number)

    def defensive_substitution(self, order, player_id, position):
        self.fielding_team.add_player(order, player_id, position, self.number)

    # Pitches.
    def pitch_list(self, pitches):
        self.current_ab.pitch_list(pitches)

    # Batter results.
    def out(self, play, rbis=0):
        # Sanity check, ensure the user isn't adding more than 3 outs.
        out_added = False
        for i in range(1, 4):
            if not self.outs[i]:
                self.outs[i] = True
                out_added = True
                break
        if not out_added:
            raise Exception("More than 3 outs in inning")

        # Add team stats for the batting team.
        if "DP" in play:
            self.batting_team.get_stats().double_plays += 1
        if "TP" in play:
            self.batting_team.get_stats().triple_plays += 1
        if "SAC" in play:
            self.batting_team.get_stats().sac_bunts += 1
        if "SF" in play:
            self.batting_team.get_stats().sac_flys += 1

        self.current_ab.out(play, rbis=rbis)

    def hit(self, bases, rbis=0):
        # Add the corresponding type of hit for the batting team.
        hit_type = 4 if bases == "U" else bases
        self.batting_team.stats.hits[hit_type] += 1

        # Unless the hit is not a home run, add a batter left on the basepaths.
        # If they get thrown out or advance to home, they will be removed.
        if hit_type != 4:
            self.batting_team.stats.left_on_base += 1

        # If the hit is a home run, check if the user gave a number of RBIs and
        # use that, otherwise add one RBI by default.
        rbis_to_add = rbis
        if hit_type == 4 and rbis_to_add == 0:
            rbis_to_add = 1

        # If the hit is a home run, add a run to the batting team.
        if hit_type == 4:
            self.batting_team.stats.runs += 1

        self.current_ab.hit(bases, rbis=rbis_to_add)

    def reach(self, play, end_base=1, rbis=0):
        # Since a batter reached base, mark them as left on base.
        # If they get thrown out or advance to home, they will be removed.
        self.batting_team.stats.left_on_base += 1
        self.current_ab.reach(play, end_base=end_base, rbis=rbis)

    # Runner results.
    def advance(self, end_base, play):
        # Check if the runner reached home plate, add the corresponding
        # statistics to the team.
        if end_base == 4 or end_base == "U":
            self.batting_team.stats.runs += 1
            self.batting_team.stats.left_on_base -= 1

        # Check if the batter stole a base, and if so, add a stolen base for
        # the batting team.
        if "SB" in play:
            self.batting_team.stats.stolen_bases += 1

        self.current_ab.advance(end_base, play)

    def thrown_out(self, out_base, play, out_number=None, pitcher_id=None):
        # Runner is no longer in the basepaths, remove them from the LOB count.
        self.batting_team.stats.left_on_base -= 1

        # Add stats to the team if the batter was thrown out caught stealing or picked off.
        if "CS" in play:
            self.batting_team.stats.caught_stealing += 1

        if "POCS" in play:
            self.batting_team.stats.caught_stealing += 1
            self.batting_team.stats.picked_off += 1

        # Record the out in either the first available out, or in the indicated out number.
        if out_number:
            if self.outs[out_number]:
                raise Exception("Indicated out for thrown_out call has already been used.")

            self.outs[out_number] = True
        else:
            out_added = False
            for i in range(1, 4):
                if not self.outs[i]:
                    self.outs[i] = True
                    out_added = True
                    break
            if not out_added:
                raise Exception("More than 3 outs in inning")

        # If the pitcher_id is passed, pass the pitcher to the at-bat object.
        responsible_pitcher = None
        if pitcher_id:
            responsible_pitcher = self.fielding_team.roster.get_player(pitcher_id)

        self.current_ab.thrown_out(out_base, play, out_number, responsible_pitcher)

    # Miscelaneous functions to detail additional events for the at-bat.
    def error(self, fielder):
        self.fielding_team.stats.errors += 1

    def balk(self):
        # Add a balk to the current pitcher. Advancements are to be handled
        # by calls to the advance method.
        self.fielding_team.get_pitcher().pitcher_stats.balks += 1

    def wp(self, quantity=1):
        self.fielding_team.get_pitcher().pitcher_stats.wild_pitches += quantity
        return None

    def pb(self, quantity=1):
        self.batting_team.stats.passed_balls += quantity
        return None

    def atbase(self, label):
        self.current_ab.atbase(label)

    def no_ab(self, label):
        # Since no at-bat occurred, when a new at-bat for the current batting
        # team is created, it should use the current batter.
        self.batting_team.no_ab()
        self.current_ab.no_ab(label)

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
