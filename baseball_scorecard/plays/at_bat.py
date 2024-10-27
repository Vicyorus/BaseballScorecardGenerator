from baseball_scorecard.plays.labeling.advance import Advance
from baseball_scorecard.plays.labeling.at_base import AtBase
from baseball_scorecard.plays.labeling.no_ab import NoAtBat
from baseball_scorecard.plays.labeling.out import Out
from baseball_scorecard.plays.labeling.pitch import Pitch
from baseball_scorecard.plays.labeling.thrown_out import ThrownOut
from baseball_scorecard.stats.inning_stats import InningStats
from baseball_scorecard.team.player import Player


class AtBat:
    def __init__(
        self,
        lineup_position: int,
        batter: Player,
        pitcher: Player,
        inning_stats: InningStats,
        is_risp: bool = False,
    ):
        self.lineup_position: int = lineup_position
        self.batter: Player = batter
        self.pitcher: Player = pitcher
        self.inning_stats: InningStats = inning_stats
        self.is_risp = is_risp

        # Add a batter faced to the pitcher.
        self.pitcher.pitcher_stats.batters_faced += 1

        self.pitches: list[Pitch] = []
        self.plays: list[Advance | AtBase | NoAtBat | Out | ThrownOut] = []
        self.count: dict[str, int] = {"b": 0, "s": 0, "f": 0}
        self.last_base_reached: int | str = 0
        self.rbis: int = 0

    # Pitches.
    def pitch_list(self, pitches: str):
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
            elif pitch in ["s", "c", "m", "l"] or (
                pitch in ["f", "t"] and self.count["s"] < 2
            ):
                self.__strike(pitch)
            # Any foul that no longer counts as a strike.
            elif pitch in ["f", "t"]:
                self.__foul(pitch)
            # Any sort of ball/pitchout.
            elif pitch in ["d", "b", "p"]:
                self.__ball(pitch)

    def __ball(self, pitch_type: str, inc_pitch_count: bool = True):
        if self.count["b"] >= 4:
            raise Exception("Ball 5 listed in pitches for at bat.")
        self.count["b"] += 1
        self.pitcher.add_pitch(is_strike=False)
        self.inning_stats.pitches += 1
        self.pitches.append(Pitch(pitch_type, inc_pitch_count, is_strike=False))

    def __strike(self, pitch_type: str, inc_pitch_count: bool = True):
        if self.count["s"] >= 3:
            raise Exception("Strike 4 listed in pitches for at bat.")
        self.count["s"] += 1
        self.pitcher.add_pitch()
        self.inning_stats.pitches += 1
        self.inning_stats.strikes += 1
        self.pitches.append(Pitch(pitch_type, inc_pitch_count))

    def __foul(self, pitch_type: str, inc_pitch_count: bool = True):
        self.count["f"] += 1
        self.pitcher.add_pitch()
        self.inning_stats.pitches += 1
        self.inning_stats.strikes += 1
        self.pitches.append(Pitch(pitch_type, inc_pitch_count))

    # Batter results.
    def out(self, play: str, out_number: int, rbis=0):
        # Check the play code to determine if additional stats have to be registered.
        has_at_bat = True
        is_strikeout = False

        # Award strikeouts to the pitcher and batter.
        if play.startswith("K") or play.startswith("!K"):
            self.pitcher.pitcher_stats.strikeouts += 1
            self.batter.batter_stats.strikeouts += 1
            self.inning_stats.strikeouts += 1
            is_strikeout = True

        # On sac flys or sac bunts, no AB is to be awarded to the batter.
        if "SAC" in play or "SF" in play:
            has_at_bat = False

        if has_at_bat:
            self.batter.batter_stats.at_bats += 1

        # If there are any RBIs, add them to the batter's stats,
        # and the at-bat's stats.
        self.batter.batter_stats.rbis += rbis
        self.rbis = rbis

        # For all non-strikeout outs, the ball has to be put in play.
        # A pitch needs to be added for these scenarios.
        if not is_strikeout:
            self.pitcher.add_pitch()
            self.inning_stats.pitches += 1
            self.inning_stats.strikes += 1
            self.pitches.append(Pitch("X", inc_pitch_count=True))

        # Add an out made to the pitcher.
        self.pitcher.pitcher_stats.outs += 1

        # Append the play to the list of plays.
        self.plays.append(Out(play, out_number))

    def hit(self, bases: int, rbis: int = 0):
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
        # the pitcher, a home run to the pitcher, an earned run
        # if it applies, and an RBI if RBIs were not specified.
        if bases == 4 or bases == "U":
            self.batter.batter_stats.runs += 1
            self.pitcher.pitcher_stats.runs += 1
            self.pitcher.pitcher_stats.home_runs += 1
            self.inning_stats.runs += 1
            if bases == 4:
                self.pitcher.pitcher_stats.earned_runs += 1
            if rbis == 0:
                self.batter.batter_stats.rbis += 1
                self.rbis = 1

        # Since all hits require a swing of the bat, add a strike to the pitch list.
        self.pitcher.add_pitch()
        self.inning_stats.pitches += 1
        self.inning_stats.strikes += 1
        self.pitches.append(Pitch("H", inc_pitch_count=True))

        # Append the play to the list of plays.
        self.plays.append(Advance(advance_label, bases, self.last_base_reached, bases))
        self.last_base_reached = bases

    def reach(self, play: str, end_base: int = 1, rbis: int = 0):
        # Some reach codes will not count as an at-bat, toggle this variable
        # when it's not applicable.
        reach_label = "Reach"
        add_at_bat = True
        add_strike = True

        # Reach on error.
        if play.upper().startswith("E"):
            reach_label = "Error"

        # Reach on strikeout.
        if play.upper() == "K":
            self.batter.batter_stats.strikeouts += 1
            self.pitcher.pitcher_stats.strikeouts += 1
            self.inning_stats.strikeouts += 1
            add_strike = False

        # Reach on walk.
        if play.upper() == "BB":
            reach_label = "Walk"
            self.batter.batter_stats.walks += 1
            self.pitcher.pitcher_stats.walks += 1
            self.inning_stats.walks += 1
            add_at_bat = False
            add_strike = False

        if play.upper() == "IBB":
            reach_label = "Intent Walk"
            self.batter.batter_stats.walks += 1
            self.pitcher.pitcher_stats.intent_walks += 1
            self.inning_stats.walks += 1
            add_at_bat = False
            add_strike = False

        # Hit by pitch.
        if play.upper() == "HP" or play.upper() == "HBP":
            reach_label = "Hit By Pitch"
            self.pitcher.pitcher_stats.hits_by_pitch += 1
            self.pitcher.add_pitch(is_strike=False)
            self.inning_stats.pitches += 1
            self.pitches.append(Pitch("R", inc_pitch_count=True, is_strike=False))
            add_at_bat = False
            add_strike = False

        # Catcher's interference.
        if play.upper() == "CI":
            reach_label = "Error"
            add_at_bat = False
            add_strike = False

        # Check if the at-bat needs to be added to the batter's stats.
        # For catcher's interference, hit by pitch and walks, no at-bat
        # is to be granted.
        if add_at_bat:
            self.batter.batter_stats.at_bats += 1

        # For reaches that are not walks, hit by pitches, strikeouts
        # and catcher's interference, the ball was put into play,
        # so a strike must be added.
        if add_strike:
            self.pitcher.add_pitch()
            self.inning_stats.pitches += 1
            self.inning_stats.strikes += 1
            self.pitches.append(Pitch("R", inc_pitch_count=True))

        # If there are any RBIs, add them to the batter's stats,
        # and the at-bat's stats.
        self.batter.batter_stats.rbis += rbis
        self.rbis = rbis

        # Append the play to the list of plays.
        self.plays.append(Advance(reach_label, play, self.last_base_reached, end_base))
        self.last_base_reached = end_base

    # Runner results.
    def advance(self, end_base: int, play: str):
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

    def thrown_out(
        self, out_base: int, play: str, out_number: int, pitcher: Player = None
    ):
        # Add the out for the pitcher.
        responsible_pitcher = pitcher if pitcher else self.pitcher
        responsible_pitcher.pitcher_stats.outs += 1

        # Append the play to the list of plays.
        self.plays.append(ThrownOut(play, self.last_base_reached, out_base, out_number))

    # Miscelaneous functions to detail additional events for the at-bat.
    def atbase(self, label: str, base: int = None):
        labeled_base = base if base else self.last_base_reached

        # Append the play to the list of plays.
        self.plays.append(AtBase(label, labeled_base))

    def no_ab(self, label: str):
        # Since the at-bat ended in an out that does not count as an appereance,
        # remove a batter faced from the pitcher.
        self.pitcher.pitcher_stats.batters_faced -= 1

        # Append the play to the list of plays.
        self.plays.append(NoAtBat(label))

    def get_metapost_data(self, inn_number: int) -> str:
        result = f"    %% inning {inn_number}, batter {self.lineup_position}\n"
        y_start = 128 * (9 - self.lineup_position)
        result += f"    ystart := {y_start};\n"
        result += "    set_vars(xstart,ystart);\n"

        result += self.__get_pitches_metapost_data()

        # Print the run dot/cross for either earned or unearned runs, respectively.
        if self.last_base_reached == 4:
            result += "    draw_dot(rundot, clr);\n"
        if self.last_base_reached == "U":
            result += "    draw_cross(rundot, clr);\n"

        # Print the RBIs.
        rbi_labels = ["rbione", "rbitwo", "rbithree", "rbifour"]
        for i in range(self.rbis):
            result += f"    draw_diamond({rbi_labels[i]}, clr);\n"

        # Print the plays.
        for play in self.plays:
            result += play.get_metapost_data()

        result += "\n"
        return result

    def __get_pitches_metapost_data(self):
        result = ""
        ball_locations = ["ballone", "balltwo", "ballthree", "ballfour"]
        strike_locations = [
            "strikeone",
            "striketwo",
            "strikethree",
            "strikefour",
            "strikefive",
            "strikesix",
            "strikeseven",
            "strikeeight",
            "strikenine",
            "striketen",
            "strikeeleven",
            "striketwelve",
            "strikethirteen",
            "strikefourteen",
            "strikefifteen",
            "strikesixteen",
            "strikeseventeen",
            "strikeeighteen",
            "strikenineteen",
            "striketwenty",
            "striketwentyone",
            "striketwentytwo",
        ]

        pitch_text_template = "    label(btex {{\\tiny {}}} etex, {}) withcolor clr;\n"
        pitch_dot_template = "    draw_strike_dot({}, clr);\n"
        pitch_circle_template = "    draw_strike_circle({}, clr);\n"

        pitch_count = 1
        count_status = {"b": 0, "s": 0, "f": 0}

        for pitch in self.pitches:
            # Break when the hit/out/reach code is found.
            if pitch.pitch_code in ["X", "H", "R"]:
                break

            # Check whether a strike, ball or foul needs to be added.
            if pitch.is_strike:
                if count_status["s"] < 22:
                    if pitch.pitch_code.upper() == "S":
                        result += pitch_dot_template.format(
                            strike_locations[count_status["s"]]
                        )
                    elif pitch.pitch_code.upper() == "C":
                        result += pitch_circle_template.format(
                            strike_locations[count_status["s"]]
                        )
                    elif pitch.pitch_code.upper() == "F":
                        result += pitch_text_template.format(
                            "X", strike_locations[count_status["s"]]
                        )
                    else:
                        result += pitch_text_template.format(
                            pitch.pitch_code.upper(),
                            strike_locations[count_status["s"]],
                        )
                    count_status["s"] += 1
            else:
                if count_status["b"] < 4:
                    result += pitch_dot_template.format(
                        ball_locations[count_status["b"]]
                    )
                    count_status["b"] += 1

            # Increment the pitch count if needed.
            if pitch.inc_pitch_count:
                pitch_count += 1

        if result != "":
            result = "    % pitches\n" + result + "    % end pitches\n"

        return result

    def __str__(self):
        result = f"{self.lineup_position}. {self.batter} vs {self.pitcher}\n"
        if len(self.pitches) != 0:
            result += f"Pitches: {' '.join(map(str, self.pitches))}\n"
        for play in self.plays:
            result += f"    {play}\n"

        result += "\n"
        return result
