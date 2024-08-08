from scorecard.plays.pitch import Pitch
from scorecard.plays.out import Out
from scorecard.plays.thrown_out import ThrownOut
from scorecard.plays.advance import Advance
from scorecard.plays.at_base import AtBase
from scorecard.plays.no_ab import NoAtBat

class AtBat():
    def __init__(self, lineup_position, batter, pitcher, inning_stats):
        self.lineup_position = lineup_position
        self.batter = batter
        self.pitcher = pitcher
        self.inning_stats = inning_stats

        # Add a batter faced to the pitcher.
        self.pitcher.pitcher_stats.batters_faced += 1

        self.pitches = []
        self.plays = []
        self.count = {"b": 0, "s": 0, "f": 0}
        self.last_base_reached = 0
        self.rbis = 0

    # Pitches.
    def pitch_list(self, pitches):
        for pitch in pitches.split(" "):
            # TODO: Consider supporting "ball in play" codes.

            # Pitcher step off and pickoff attempts, does not count for any
            # statistic at the moment.
            if pitch in ["pso", "1", "2", "3"]:
                continue
            # Pitcher pitch clock violation.
            elif pitch == "vp":
                self.__ball(pitch, inc_pitch_count=False)
            # Batter pitch clock violation.
            elif pitch == "ab":
                self.__strike(pitch, inc_pitch_count=False)
            # Any sort of strike.
            elif pitch in ["s", "c", "m", "l"] or (pitch in ["f", "t"] and self.count["s"] < 2):
                self.__strike(pitch)
            # Any foul that no longer counts as a strike.
            elif pitch in ["f", "t"]:
                self.__foul(pitch)
            # Any sort of ball/pitchout.
            elif pitch in ["d", "b", "p"]:
                self.__ball(pitch)

    def __ball(self, pitch_type, inc_pitch_count=True):
        if self.count["b"] >= 3:
            raise Exception("Ball 4 listed in pitches for at bat.")
        self.count["b"] += 1
        self.pitcher.add_pitch(is_strike=False)
        self.inning_stats.pitches += 1
        self.pitches.append(Pitch(pitch_type, inc_pitch_count, is_strike=False))

    def __strike(self, pitch_type, inc_pitch_count=True):
        if self.count["s"] >= 2:
            raise Exception("Strike 3 listed in pitches for at bat.")
        self.count["s"] += 1
        self.pitcher.add_pitch(is_strike=True)
        self.inning_stats.pitches += 1
        self.inning_stats.strikes += 1
        self.pitches.append(Pitch(pitch_type, inc_pitch_count))

    def __foul(self, pitch_type, inc_pitch_count=True):
        self.count["f"] += 1
        self.pitcher.add_pitch(is_strike=True)
        self.inning_stats.pitches += 1
        self.inning_stats.strikes += 1
        self.pitches.append(Pitch(pitch_type, inc_pitch_count))

    # Batter results.
    def out(self, play, out_number, rbis=0):
        # Check the play code to determine if additional stats have to be registered.
        has_at_bat = True

        # Award strikeouts to the pitcher and batter.
        if play.startswith("K") or play.startswith("!K"):
            self.pitcher.pitcher_stats.strikeouts += 1
            self.batter.batter_stats.strikeouts += 1
            self.inning_stats.strikeouts += 1

        # On sac flys or sac bunts, no AB is to be awarded to the batter.
        if "SAC" in play or "SF" in play:
            has_at_bat = False

        if has_at_bat:
            self.batter.batter_stats.at_bats += 1

        # If there are any RBIs, add them to the batter's stats,
        # and the at-bat's stats.
        self.batter.batter_stats.rbis += rbis
        self.rbis = rbis

        # Since all outs to the batter require a swing of the bat,
        # add a strike to the pitch list.
        self.pitcher.add_pitch(is_strike=True)
        self.inning_stats.pitches += 1
        self.inning_stats.strikes += 1
        self.pitches.append(Pitch('X', inc_pitch_count=True))

        # Add an out made to the pitcher.
        self.pitcher.pitcher_stats.outs += 1

        # Append the play to the list of plays.
        self.plays.append(Out(play, out_number))

    def hit(self, bases, rbis=0):
        # Set the advance label as a hit. This can be overridden if there's a home run.
        advance_label = "Hit"

        # Record the hit for both the batter and the pitcher, and the at-bat
        # for the batter.
        self.batter.batter_stats.hits += 1
        self.batter.batter_stats.at_bats += 1
        self.pitcher.pitcher_stats.hits += 1
        self.inning_stats.hits += 1

        # If there are any RBIs, add them to the batter's stats,
        # and the at-bat's stats.
        self.batter.batter_stats.rbis += rbis
        self.rbis = rbis

        # If the hit is a home run, add a run to the batter and
        # the pitcher, a home run to the pitcher, and an earned run
        # if it applies.
        if bases == 4 or bases == "U":
            self.batter.batter_stats.runs += 1
            self.pitcher.pitcher_stats.runs += 1
            self.pitcher.pitcher_stats.home_runs += 1
            self.inning_stats.runs += 1
            if bases == 4:
                self.pitcher.pitcher_stats.earned_runs += 1

        # Since all hits require a swing of the bat, add a strike to the pitch list.
        self.pitcher.add_pitch(is_strike=True)
        self.inning_stats.pitches += 1
        self.inning_stats.strikes += 1
        self.pitches.append(Pitch('H', inc_pitch_count=True))

        # Append the play to the list of plays.
        self.plays.append(Advance(advance_label, bases, self.last_base_reached, bases))
        self.last_base_reached = bases

    def reach(self, play, end_base=1, rbis=0):
        # Some reach codes will not count as an at-bat, toggle this variable
        # when it's not applicable.
        reach_label = "Reach"
        add_at_bat = True

        # Reach on error.
        if play.upper().startswith("E"):
            reach_label = "Error"

        # Reach on strikeout.
        if play.upper() == "K":
            self.batter.batter_stats.strikeouts += 1
            self.pitcher.pitcher_stats.strikeouts += 1
            self.inning_stats.strikeouts += 1

        # Reach on walk.
        if play.upper() == "BB":
            reach_label = "Walk"
            self.batter.batter_stats.walks += 1
            self.pitcher.pitcher_stats.walks += 1
            self.inning_stats.walks += 1
            self.pitcher.add_pitch(is_strike=False)
            self.inning_stats.pitches += 1
            self.pitches.append(Pitch('R', inc_pitch_count=True, is_strike=False))
            add_at_bat = False

        if play.upper() == "IBB":
            reach_label = "Intent Walk"
            self.batter.batter_stats.walks += 1
            self.pitcher.pitcher_stats.intent_walks += 1
            self.inning_stats.walks += 1
            self.pitcher.add_pitch(is_strike=False)
            self.inning_stats.pitches += 1
            self.pitches.append(Pitch('R', inc_pitch_count=True, is_strike=False))
            add_at_bat = False

        # Hit by pitch.
        if play.upper() == "HP" or play.upper() == "HBP":
            self.pitcher.pitcher_stats.hits_by_pitch += 1
            self.pitcher.add_pitch(is_strike=False)
            self.inning_stats.pitches += 1
            self.pitches.append(Pitch('R', inc_pitch_count=True, is_strike=False))
            add_at_bat = False

        # Catcher's interference.
        if play.upper() == "CI":
            reach_label = "Error"
            add_at_bat = False

        # If an at-bat needs to be added, add the at-bat, and a strike.
        # Barring walks and catcher's interference, reach cases imply the ball
        # has been put to play (or is a dropped strike 3).
        if add_at_bat:
            self.pitcher.add_pitch(is_strike=True)
            self.inning_stats.pitches += 1
            self.inning_stats.strikes += 1
            self.pitches.append(Pitch('R', inc_pitch_count=True))
            self.batter.batter_stats.at_bats += 1

        # If there are any RBIs, add them to the batter's stats,
        # and the at-bat's stats.
        self.batter.batter_stats.rbis += rbis
        self.rbis = rbis

        # Append the play to the list of plays.
        self.plays.append(Advance(reach_label, play, self.last_base_reached, end_base))
        self.last_base_reached = end_base

    # Runner results.
    def advance(self, end_base, play):
        # Check if the runner reached home plate, add the corresponding
        # statistics to the batter/pitcher.
        if end_base == 4 or end_base == "U":
            self.batter.batter_stats.runs += 1
            self.pitcher.pitcher_stats.runs += 1
            self.inning_stats.runs += 1
            if end_base == 4:
                self.pitcher.pitcher_stats.earned_runs += 1

        # Append the play to the list of plays.
        self.plays.append(Advance("Advance", play, self.last_base_reached, end_base))
        self.last_base_reached = end_base

    def thrown_out(self, out_base, play, out_number, pitcher=None):
        # Add the out for the pitcher.
        responsible_pitcher = pitcher if pitcher else self.pitcher
        responsible_pitcher.pitcher_stats.outs += 1

        # Append the play to the list of plays.
        self.plays.append(ThrownOut(play, self.last_base_reached, out_base, out_number))

    # Miscelaneous functions to detail additional events for the at-bat.
    def atbase(self, label, base):
        labeled_base = base if base else self.last_base_reached

        # Append the play to the list of plays.
        self.plays.append(AtBase(label, labeled_base))

    def no_ab(self, label):
        # Since the at-bat ended in an out that does not count as an appereance,
        # remove a batter faced from the pitcher.
        self.pitcher.pitcher_stats.batters_faced -= 1

        # Append the play to the list of plays.
        self.plays.append(NoAtBat(label))

    def get_metapost_data(self, inn_number):
        result = f"    %% inning {inn_number}, batter {self.lineup_position}\n"
        y_start = 128 * (9 - self.lineup_position)
        result += f"    ystart := {y_start};\n"
        result += "    set_vars(xstart,ystart);\n"

        result += self.__get_pitches_metapost_data()

        # Print the run dot/cross for either earned or unearned runs, respectively.
        if self.last_base_reached == 4:
            result += "    draw_dot(rundot, clr);"
        if self.last_base_reached == "U":
            result += "    draw_cross(rundot, clr);"

        # Print the RBIs.
        rbi_labels = ["rbione", "rbitwo", "rbithree", "rbifour"]
        for i in range(self.rbis):
            result += f"    draw_dot({rbi_labels[i]}, clr);\n"

        # Print the plays.
        for play in self.plays:
            result += play.get_metapost_data()

        result += "\n"
        return result

    def __get_pitches_metapost_data(self):
        result = "    % pitches\n"
        ball_locations = ["ballone", "balltwo", "ballthree"]
        strike_locations = ["strikeone", "striketwo"]
        foul_locations = ["foulone", "foultwo", "foulthree", "foulfour"]

        pitch_template = "    label(btex {{\\sf {}}} etex, {}) withcolor clr;\n"
        pitch_count = 1
        count_status = {
            "b": 0,
            "s": 0,
            "f": 0
        }

        for pitch in self.pitches:
            # Break when the hit/out/reach code is found.
            if pitch.pitch_code in ["X", "H", "R"]:
                break

            # Check whether a strike, ball or foul needs to be added.
            if pitch.is_strike:
                if count_status["s"] < 2:
                    result += pitch_template.format(pitch_count, strike_locations[count_status["s"]])
                    count_status["s"] += 1
                else:
                    if count_status["f"] < 4:
                        result += pitch_template.format("x", foul_locations[count_status["f"]])
                        count_status["f"] += 1
            else:
                if count_status["b"] < 3:
                    result += pitch_template.format(pitch_count, ball_locations[count_status["b"]])
                    count_status["b"] += 1

            # Increment the pitch count if needed.
            if pitch.inc_pitch_count:
                pitch_count += 1

        return result

    def __str__(self):
        result = f'{self.lineup_position}. {self.batter} vs {self.pitcher}\n'
        result += f'Pitches: {len(self.pitches)}\n'
        for play in self.plays:
            result += f'    {play}\n'

        result += "\n"
        return result
