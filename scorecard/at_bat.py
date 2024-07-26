from scorecard.pitch import Pitch

class AtBat():
    def __init__(self, batter, pitcher):
        self.batter = batter
        self.pitcher = pitcher

        self.pitches = []
        self.plays = []
        self.count = {"b": 0, "s": 0, "f": 0}
        self.rbis = 0

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
        self.pitches.append(Pitch(pitch_type, inc_pitch_count, is_strike=False))

    def __strike(self, pitch_type, inc_pitch_count=True):
        if self.count["s"] >= 2:
            raise Exception("Strike 3 listed in pitches for at bat.")
        self.count["s"] += 1
        self.pitches.append(Pitch(pitch_type, inc_pitch_count))

    def __foul(self, pitch_type, inc_pitch_count=True):
        self.count["f"] += 1
        self.pitches.append(Pitch(pitch_type, inc_pitch_count))

    def out(self, play):
        # Check the play code to determine if additional stats have to be registered.
        has_at_bat = True

        # Award strikeouts to the pitcher and batter.
        if play.startswith("K") or play.startswith("!K"):
            self.pitcher.pitcher_stats.strikeouts += 1
            self.batter.batter_stats.strikeouts += 1

        # On sac flys or sac bunts, no AB is to be awarded to the batter.
        if "SAC" in play or "SF" in play:
            has_at_bat = False

        if has_at_bat:
            self.batter.batter_stats.at_bats += 1

        # Since all outs to the batter require a swing of the bat,
        # add a strike to the pitch list.
        self.pitches.append(Pitch('X', inc_pitch_count=True, is_strike=True))

        # Add an out made to the pitcher.
        self.pitcher.pitcher_stats.outs += 1

        # TODO: Add play to the list of plays for this batter.

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
        result = f'{self.batter} vs {self.pitcher}\n'
        result += f'Pitches: {len(self.pitches)}\n'

        return result
