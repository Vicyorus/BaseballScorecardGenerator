import pytest
from baseball_scorecard.plays.at_bat import AtBat
from baseball_scorecard.team.player import Player
from baseball_scorecard.stats.inning_stats import InningStats
from baseball_scorecard.plays.labeling.advance import Advance
from baseball_scorecard.plays.labeling.at_base import AtBase
from baseball_scorecard.plays.labeling.no_ab import NoAtBat
from baseball_scorecard.plays.labeling.out import Out
from baseball_scorecard.plays.labeling.pitch import Pitch
from baseball_scorecard.plays.labeling.thrown_out import ThrownOut


class TestAtBat:
    """Tests the AtBat class."""

    @pytest.fixture(autouse=True)
    def setup_at_bat_data(self):
        self._batter = Player(1, 1, "John Doe")
        self._pitcher = Player(2, 2, "Jack Doe")

    @pytest.mark.parametrize(
        "pitch_string, expected_count",
        [
            ("c c c", {"b": 0, "s": 3, "f": 0}),
            ("b b b b", {"b": 4, "s": 0, "f": 0}),
            ("c b c b b b c", {"b": 4, "s": 3, "f": 0}),
            ("s s f f f f f f f s", {"b": 0, "s": 3, "f": 7}),
        ],
    )
    def test_pitch_list(self, pitch_string, expected_count):
        """Test that the pitch_list method is correct."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.pitch_list(pitch_string)

        assert at_bat.count == expected_count
        assert (
            at_bat.pitcher.pitcher_stats.strikes
            == expected_count["s"] + expected_count["f"]
        )
        assert (
            at_bat.pitcher.pitcher_stats.pitches
            == expected_count["b"] + expected_count["s"] + expected_count["f"]
        )
        assert at_bat.inning_stats.strikes == expected_count["s"] + expected_count["f"]
        assert (
            at_bat.inning_stats.pitches
            == expected_count["b"] + expected_count["s"] + expected_count["f"]
        )
        assert (
            len(at_bat.pitches)
            == expected_count["b"] + expected_count["s"] + expected_count["f"]
        )

    def test_pitch_list_strike_exception(self):
        """Test that the pitch_list method raises an exception when more than 3 strikes are registered."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        with pytest.raises(Exception):
            at_bat.pitch_list("s s s s")

    def test_pitch_list_ball_exception(self):
        """Test that the pitch_list method raises an exception when more than 4 balls are registered."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        with pytest.raises(Exception):
            at_bat.pitch_list("b b b b b")

    def test_out(self):
        """Test that the out method is correct."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.out("G3", 1)

        assert at_bat.batter.batter_stats.at_bats == 1
        assert at_bat.inning_stats.pitches == 1
        assert at_bat.inning_stats.strikes == 1
        assert at_bat.pitcher.pitcher_stats.outs == 1
        assert at_bat.pitcher.pitcher_stats.pitches == 1
        assert at_bat.pitcher.pitcher_stats.strikes == 1
        assert len(at_bat.pitches) == 1
        assert type(at_bat.plays[0]) == Out

    @pytest.mark.parametrize(
        "strikeout_type",
        [
            ("K"),
            ("!K"),
        ],
    )
    def test_out_strikeout(self, strikeout_type):
        """Test that the out method is correct, for strike outs."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.out(strikeout_type, 1)

        assert at_bat.batter.batter_stats.at_bats == 1
        assert at_bat.batter.batter_stats.strikeouts == 1
        assert at_bat.inning_stats.pitches == 0
        assert at_bat.inning_stats.strikes == 0
        assert at_bat.inning_stats.strikeouts == 1
        assert at_bat.pitcher.pitcher_stats.outs == 1
        assert at_bat.pitcher.pitcher_stats.pitches == 0
        assert at_bat.pitcher.pitcher_stats.strikes == 0
        assert at_bat.pitcher.pitcher_stats.strikeouts == 1
        assert len(at_bat.pitches) == 0
        assert type(at_bat.plays[0]) == Out

    @pytest.mark.parametrize(
        "sacrifice_type",
        [
            ("SAC1-3"),
            ("SF8"),
        ],
    )
    def test_out_sacrifice(self, sacrifice_type):
        """Test that the out method is correct, for sacrifice outs."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.out(sacrifice_type, 1)

        assert at_bat.batter.batter_stats.at_bats == 0
        assert at_bat.inning_stats.pitches == 1
        assert at_bat.inning_stats.strikes == 1
        assert at_bat.pitcher.pitcher_stats.outs == 1
        assert at_bat.pitcher.pitcher_stats.pitches == 1
        assert at_bat.pitcher.pitcher_stats.strikes == 1
        assert len(at_bat.pitches) == 1
        assert type(at_bat.plays[0]) == Out

    def test_out_rbis(self):
        """Test that the out method adds the correct amount of RBIs to the corresponding statistics."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.out("G3", 1, rbis=3)

        assert at_bat.rbis == 3
        assert at_bat.batter.batter_stats.rbis == 3

    @pytest.mark.parametrize(
        "hit_type",
        [
            (1),
            (2),
            (3),
        ],
    )
    def test_hit(self, hit_type):
        """Test that the hit method is correct."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.hit(hit_type)

        assert at_bat.batter.batter_stats.hits == 1
        assert at_bat.batter.batter_stats.at_bats == 1
        assert at_bat.pitcher.pitcher_stats.pitches == 1
        assert at_bat.pitcher.pitcher_stats.strikes == 1
        assert at_bat.pitcher.pitcher_stats.hits == 1
        assert at_bat.inning_stats.hits == 1
        assert at_bat.last_base_reached == hit_type
        assert len(at_bat.pitches) == 1
        assert type(at_bat.plays[0]) == Advance
        assert at_bat.plays[0].advance_code == "Hit"

    def test_hit_earned_home_run(self):
        """Test that the hit method is correct, when an earned home run occurs."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.hit(4)

        assert at_bat.batter.batter_stats.runs == 1
        assert at_bat.batter.batter_stats.rbis == 1
        assert at_bat.pitcher.pitcher_stats.runs == 1
        assert at_bat.pitcher.pitcher_stats.home_runs == 1
        assert at_bat.inning_stats.runs == 1
        assert at_bat.batter.batter_stats.hits == 1
        assert at_bat.batter.batter_stats.at_bats == 1
        assert at_bat.pitcher.pitcher_stats.pitches == 1
        assert at_bat.pitcher.pitcher_stats.strikes == 1
        assert at_bat.pitcher.pitcher_stats.hits == 1
        assert at_bat.pitcher.pitcher_stats.earned_runs == 1
        assert at_bat.inning_stats.hits == 1
        assert at_bat.last_base_reached == 4
        assert at_bat.rbis == 1
        assert len(at_bat.pitches) == 1
        assert type(at_bat.plays[0]) == Advance
        assert at_bat.plays[0].advance_code == "Hit"

    def test_hit_unearned_home_run(self):
        """Test that the hit method is correct, when an unearned home run occurs."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.hit("U")

        assert at_bat.batter.batter_stats.runs == 1
        assert at_bat.batter.batter_stats.rbis == 1
        assert at_bat.pitcher.pitcher_stats.runs == 1
        assert at_bat.pitcher.pitcher_stats.home_runs == 1
        assert at_bat.inning_stats.runs == 1
        assert at_bat.batter.batter_stats.hits == 1
        assert at_bat.batter.batter_stats.at_bats == 1
        assert at_bat.pitcher.pitcher_stats.pitches == 1
        assert at_bat.pitcher.pitcher_stats.strikes == 1
        assert at_bat.pitcher.pitcher_stats.hits == 1
        assert at_bat.inning_stats.hits == 1
        assert at_bat.last_base_reached == "U"
        assert at_bat.rbis == 1
        assert len(at_bat.pitches) == 1
        assert type(at_bat.plays[0]) == Advance
        assert at_bat.plays[0].advance_code == "Hit"

    def test_hit_rbis(self):
        """Test that the hit method adds the correct amount of RBIs to the corresponding statistics."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.hit("G3", rbis=3)

        assert at_bat.rbis == 3
        assert at_bat.batter.batter_stats.rbis == 3

    def test_reach(self):
        """Test that the reach method is correct."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.reach("FC5-4")

        assert at_bat.batter.batter_stats.at_bats == 1
        assert at_bat.pitcher.pitcher_stats.pitches == 1
        assert at_bat.pitcher.pitcher_stats.strikes == 1
        assert at_bat.last_base_reached == 1
        assert len(at_bat.pitches) == 1
        assert type(at_bat.plays[0]) == Advance
        assert at_bat.plays[0].advance_code == "Reach"

    def test_reach_defense_error(self):
        """Test that the reach method is correct, when a batter reaches on an error."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.reach("E4")

        assert at_bat.batter.batter_stats.at_bats == 1
        assert at_bat.pitcher.pitcher_stats.pitches == 1
        assert at_bat.pitcher.pitcher_stats.strikes == 1
        assert at_bat.last_base_reached == 1
        assert len(at_bat.pitches) == 1
        assert type(at_bat.plays[0]) == Advance
        assert at_bat.plays[0].advance_code == "Error"

    def test_reach_strikeout(self):
        """Test that the reach method is correct, when a batter reaches on a strikeout."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.reach("K")

        assert at_bat.batter.batter_stats.strikeouts == 1
        assert at_bat.pitcher.pitcher_stats.strikeouts == 1
        assert at_bat.inning_stats.strikeouts == 1
        assert at_bat.batter.batter_stats.at_bats == 1
        assert at_bat.pitcher.pitcher_stats.pitches == 0
        assert at_bat.pitcher.pitcher_stats.strikes == 0
        assert at_bat.last_base_reached == 1
        assert len(at_bat.pitches) == 0
        assert type(at_bat.plays[0]) == Advance
        assert at_bat.plays[0].advance_code == "Reach"

    def test_reach_walk(self):
        """Test that the reach method is correct, when a batter reaches on a walk."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.reach("BB")

        assert at_bat.batter.batter_stats.walks == 1
        assert at_bat.pitcher.pitcher_stats.walks == 1
        assert at_bat.inning_stats.walks == 1
        assert at_bat.batter.batter_stats.at_bats == 0
        assert at_bat.pitcher.pitcher_stats.pitches == 0
        assert at_bat.pitcher.pitcher_stats.strikes == 0
        assert at_bat.last_base_reached == 1
        assert len(at_bat.pitches) == 0
        assert type(at_bat.plays[0]) == Advance
        assert at_bat.plays[0].advance_code == "Walk"

    def test_reach_intent_walk(self):
        """Test that the reach method is correct, when a batter reaches on an intent walk."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.reach("IBB")

        assert at_bat.batter.batter_stats.walks == 1
        assert at_bat.pitcher.pitcher_stats.intent_walks == 1
        assert at_bat.inning_stats.walks == 1
        assert at_bat.batter.batter_stats.at_bats == 0
        assert at_bat.pitcher.pitcher_stats.pitches == 0
        assert at_bat.pitcher.pitcher_stats.strikes == 0
        assert at_bat.last_base_reached == 1
        assert len(at_bat.pitches) == 0
        assert type(at_bat.plays[0]) == Advance
        assert at_bat.plays[0].advance_code == "Intent Walk"

    @pytest.mark.parametrize(
        "hbp_label",
        [
            ("HBP"),
            ("HP"),
        ],
    )
    def test_reach_hit_by_pitch(self, hbp_label):
        """Test that the reach method is correct, when a batter reaches on a hit by pitch."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.reach(hbp_label)

        assert at_bat.pitcher.pitcher_stats.hits_by_pitch == 1
        assert at_bat.batter.batter_stats.at_bats == 0
        assert at_bat.pitcher.pitcher_stats.pitches == 1
        assert at_bat.pitcher.pitcher_stats.strikes == 0
        assert at_bat.last_base_reached == 1
        assert len(at_bat.pitches) == 1
        assert type(at_bat.plays[0]) == Advance
        assert at_bat.plays[0].advance_code == "Hit By Pitch"

    def test_reach_catcher_interference(self):
        """Test that the reach method is correct, when a batter reaches on a catcher's interference."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.reach("CI")

        assert at_bat.batter.batter_stats.at_bats == 0
        assert at_bat.pitcher.pitcher_stats.pitches == 0
        assert at_bat.pitcher.pitcher_stats.strikes == 0
        assert at_bat.last_base_reached == 1
        assert len(at_bat.pitches) == 0
        assert type(at_bat.plays[0]) == Advance
        assert at_bat.plays[0].advance_code == "Error"

    def test_reach_rbis(self):
        """Test that the reach method adds the correct amount of RBIs to the corresponding statistics."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.reach("FC5", rbis=3)

        assert at_bat.rbis == 3
        assert at_bat.batter.batter_stats.rbis == 3

    def test_advance(self):
        """Test that the reach method is correct."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.last_base_reached = 1
        at_bat.advance(2, "3 1B")

        assert type(at_bat.plays[0]) == Advance
        assert at_bat.plays[0].advance_code == "Advance"
        assert at_bat.plays[0].play == "3 1B"
        assert at_bat.plays[0].start == 1
        assert at_bat.plays[0].end == 2
        assert at_bat.batter.batter_stats.runs == 0
        assert at_bat.pitcher.pitcher_stats.runs == 0
        assert at_bat.pitcher.pitcher_stats.earned_runs == 0
        assert at_bat.inning_stats.runs == 0

    def test_advance_earned_run(self):
        """Test that the reach method is correct when an earned run is scored."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.last_base_reached = 3
        at_bat.advance(4, "3 1B")

        assert type(at_bat.plays[0]) == Advance
        assert at_bat.plays[0].advance_code == "Advance"
        assert at_bat.plays[0].play == "3 1B"
        assert at_bat.plays[0].start == 3
        assert at_bat.plays[0].end == 4
        assert at_bat.batter.batter_stats.runs == 1
        assert at_bat.pitcher.pitcher_stats.runs == 1
        assert at_bat.pitcher.pitcher_stats.earned_runs == 1
        assert at_bat.inning_stats.runs == 1

    def test_advance_unearned_run(self):
        """Test that the reach method is correct when an unearned run is scored."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.last_base_reached = 3
        at_bat.advance("U", "3 1B")

        assert type(at_bat.plays[0]) == Advance
        assert at_bat.plays[0].advance_code == "Advance"
        assert at_bat.plays[0].play == "3 1B"
        assert at_bat.plays[0].start == 3
        assert at_bat.plays[0].end == "U"
        assert at_bat.batter.batter_stats.runs == 1
        assert at_bat.pitcher.pitcher_stats.runs == 1
        assert at_bat.pitcher.pitcher_stats.earned_runs == 0
        assert at_bat.inning_stats.runs == 1

    def test_thrown_out_default_pitcher(self):
        """Test that the reach method is correct, and uses the at-bat's pitcher."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.last_base_reached = 1
        at_bat.thrown_out(2, "3 FC5-4", 1)

        assert type(at_bat.plays[0]) == ThrownOut
        assert at_bat.plays[0].play == "3 FC5-4"
        assert at_bat.plays[0].start == 1
        assert at_bat.plays[0].end == 2
        assert at_bat.plays[0].out_number == 1
        assert self._pitcher.pitcher_stats.outs == 1

    def test_thrown_out_different_pitcher(self):
        """Test that the reach method is correct, and uses the designated pitcher instead of the at-bat's."""
        new_pitcher = Player(4, 4, "James Doe")
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.last_base_reached = 1
        at_bat.thrown_out(2, "3 FC5-4", 1, pitcher=new_pitcher)

        assert type(at_bat.plays[0]) == ThrownOut
        assert at_bat.plays[0].play == "3 FC5-4"
        assert at_bat.plays[0].start == 1
        assert at_bat.plays[0].end == 2
        assert at_bat.plays[0].out_number == 1
        assert self._pitcher.pitcher_stats.outs == 0
        assert new_pitcher.pitcher_stats.outs == 1

    def test_atbase_default_base(self):
        """Test that the atbase method is correct, when using the default base."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.last_base_reached = 1
        at_bat.atbase("PR")

        assert type(at_bat.plays[0]) == AtBase
        assert at_bat.plays[0].label == "PR"
        assert at_bat.plays[0].base == 1

    def test_atbase_specific_base(self):
        """Test that the atbase method is correct, when using a specific base."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.last_base_reached = 1
        at_bat.atbase("PR", 2)

        assert type(at_bat.plays[0]) == AtBase
        assert at_bat.plays[0].label == "PR"
        assert at_bat.plays[0].base == 2

    def test_no_ab(self):
        """Test that the no_ab method is correct."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.no_ab("CS")

        assert type(at_bat.plays[0]) == NoAtBat
        assert at_bat.plays[0].play == "CS"
        assert self._pitcher.pitcher_stats.batters_faced == 0

    def test_get_metapost_data_pitch_list(self):
        """Test that the get_metapost_data method is correct when the pitch_list method has been called."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.pitch_list("s s f f f f f f f f f f f f f f f f f f f f f b b b b")

        expected_metapost = (
            "    %% inning 1, batter 1\n"
            "    ystart := 1024;\n"
            "    set_vars(xstart,ystart);\n"
            "    % pitches\n"
            "    draw_strike_dot(strikeone, clr);\n"
            "    draw_strike_dot(striketwo, clr);\n"
            "    label(btex {\\tiny X} etex, strikethree) withcolor clr;\n"
            "    label(btex {\\tiny X} etex, strikefour) withcolor clr;\n"
            "    label(btex {\\tiny X} etex, strikefive) withcolor clr;\n"
            "    label(btex {\\tiny X} etex, strikesix) withcolor clr;\n"
            "    label(btex {\\tiny X} etex, strikeseven) withcolor clr;\n"
            "    label(btex {\\tiny X} etex, strikeeight) withcolor clr;\n"
            "    label(btex {\\tiny X} etex, strikenine) withcolor clr;\n"
            "    label(btex {\\tiny X} etex, striketen) withcolor clr;\n"
            "    label(btex {\\tiny X} etex, strikeeleven) withcolor clr;\n"
            "    label(btex {\\tiny X} etex, striketwelve) withcolor clr;\n"
            "    label(btex {\\tiny X} etex, strikethirteen) withcolor clr;\n"
            "    label(btex {\\tiny X} etex, strikefourteen) withcolor clr;\n"
            "    label(btex {\\tiny X} etex, strikefifteen) withcolor clr;\n"
            "    label(btex {\\tiny X} etex, strikesixteen) withcolor clr;\n"
            "    label(btex {\\tiny X} etex, strikeseventeen) withcolor clr;\n"
            "    label(btex {\\tiny X} etex, strikeeighteen) withcolor clr;\n"
            "    label(btex {\\tiny X} etex, strikenineteen) withcolor clr;\n"
            "    label(btex {\\tiny X} etex, striketwenty) withcolor clr;\n"
            "    label(btex {\\tiny X} etex, striketwentyone) withcolor clr;\n"
            "    label(btex {\\tiny X} etex, striketwentytwo) withcolor clr;\n"
            "    draw_strike_dot(ballone, clr);\n"
            "    draw_strike_dot(balltwo, clr);\n"
            "    draw_strike_dot(ballthree, clr);\n"
            "    draw_strike_dot(ballfour, clr);\n"
            "    % end pitches\n\n"
        )

        assert at_bat.get_metapost_data(1) == expected_metapost

    def test_get_metapost_data_out(self):
        """Test that the get_metapost_data method is correct when an out is recorded for the batter."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.out("G3", 1)

        expected_metapost = (
            "    %% inning 1, batter 1\n"
            "    ystart := 1024;\n"
            "    set_vars(xstart,ystart);\n"
            "    label(btex {\\bigsf G3} etex, outlabel) withcolor outclr;\n"
            "    draw_out_one(xstart,ystart,clr);\n\n"
        )

        assert at_bat.get_metapost_data(1) == expected_metapost

    @pytest.mark.parametrize(
        "hit, expected_play, expected_basepath",
        [
            (1, "1B", "single"),
            (2, "2B", "double"),
            (3, "3B", "triple"),
        ],
    )
    def test_get_metapost_data_hit(self, hit, expected_play, expected_basepath):
        """Test that the get_metapost_data method is correct when the batter gets a hit."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.hit(hit)

        expected_metapost = (
            "    %% inning 1, batter 1\n"
            "    ystart := 1024;\n"
            "    set_vars(xstart,ystart);\n"
            f"    label(btex {{\\midsf {expected_play}}} etex, playloc) withcolor hit;\n"
            f"    draw({expected_basepath}) withcolor hit;\n\n"
        )

        assert at_bat.get_metapost_data(1) == expected_metapost

    @pytest.mark.parametrize(
        "hit, expected_run_symbol",
        [
            (4, "draw_dot"),
            ("U", "draw_cross"),
        ],
    )
    def test_get_metapost_data_homerun(self, hit, expected_run_symbol):
        """Test that the get_metapost_data method is correct when the batter gets a home run."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.hit(hit)

        expected_metapost = (
            "    %% inning 1, batter 1\n"
            "    ystart := 1024;\n"
            "    set_vars(xstart,ystart);\n"
            f"    {expected_run_symbol}(rundot, clr);\n"
            "    draw_diamond(rbione, clr);\n"
            "    label(btex {\\midsf HR} etex, playloc) withcolor homer;\n"
            "    draw(homerun) withcolor homer;\n\n"
        )

        assert at_bat.get_metapost_data(1) == expected_metapost

    def test_get_metapost_data_reach(self):
        """Test that the get_metapost_data method is correct when the batter reaches base."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.reach("FC5")

        expected_metapost = (
            "    %% inning 1, batter 1\n"
            "    ystart := 1024;\n"
            "    set_vars(xstart,ystart);\n"
            "    label.lrt(btex {\\sf FC5} etex, wayfirst) withcolor clr;\n"
            "    draw(single) withcolor clr;\n\n"
        )

        assert at_bat.get_metapost_data(1) == expected_metapost

    def test_get_metapost_data_error(self):
        """Test that the get_metapost_data method is correct when the batter reaches on an error."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.reach("E1")

        expected_metapost = (
            "    %% inning 1, batter 1\n"
            "    ystart := 1024;\n"
            "    set_vars(xstart,ystart);\n"
            "    label.lrt(btex {\\sf E1} etex, wayfirst) withcolor clr;\n"
            "    draw(single) withcolor error;\n\n"
        )

        assert at_bat.get_metapost_data(1) == expected_metapost

    def test_get_metapost_data_strikeout(self):
        """Test that the get_metapost_data method is correct when the batter reaches on a strikeout."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.reach("K")

        expected_metapost = (
            "    %% inning 1, batter 1\n"
            "    ystart := 1024;\n"
            "    set_vars(xstart,ystart);\n"
            "    label.lrt(btex {\\sf K} etex, wayfirst) withcolor clr;\n"
            "    draw(single) withcolor clr;\n\n"
        )

        assert at_bat.get_metapost_data(1) == expected_metapost

    @pytest.mark.parametrize(
        "walk_type",
        [
            ("BB"),
            ("IBB"),
        ],
    )
    def test_get_metapost_data_walk(self, walk_type):
        """Test that the get_metapost_data method is correct when the batter reaches on a walk."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.reach(walk_type)

        expected_metapost = (
            "    %% inning 1, batter 1\n"
            "    ystart := 1024;\n"
            "    set_vars(xstart,ystart);\n"
            f"    label(btex {{\\midsf {walk_type}}} etex, playloc) withcolor walk;\n"
            "    draw(single) withcolor walk;\n\n"
        )

        assert at_bat.get_metapost_data(1) == expected_metapost

    @pytest.mark.parametrize(
        "end_base, metapost_data",
        [
            (
                2,
                {
                    "location": ".urt",
                    "label_loc": "waysecond",
                    "draw_loc": "firstsecond",
                },
            ),
            (
                3,
                {
                    "location": ".ulft",
                    "label_loc": "waythird",
                    "draw_loc": "firstthird",
                },
            ),
        ],
    )
    def test_get_metapost_data_advance_as_batter(self, end_base, metapost_data):
        """Test that the get_metapost_data method is correct when the batter-runner advances."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.last_base_reached = 1
        at_bat.advance(end_base, "E1")

        expected_metapost = (
            "    %% inning 1, batter 1\n"
            "    ystart := 1024;\n"
            "    set_vars(xstart,ystart);\n"
            f"    label{metapost_data['location']}(btex {{\\sf E1}} etex, {metapost_data['label_loc']}) withcolor clr;\n"
            f"    draw({metapost_data['draw_loc']}) withcolor clr;\n\n"
        )

        assert at_bat.get_metapost_data(1) == expected_metapost

    @pytest.mark.parametrize(
        "end_base, expected_run_symbol",
        [
            (4, "draw_dot"),
            ("U", "draw_cross"),
        ],
    )
    def test_get_metapost_data_advance_as_batter_score(
        self, end_base, expected_run_symbol
    ):
        """Test that the get_metapost_data method is correct when the batter-runner advances and scores."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.last_base_reached = 1
        at_bat.advance(end_base, "E1")

        expected_metapost = (
            "    %% inning 1, batter 1\n"
            "    ystart := 1024;\n"
            "    set_vars(xstart,ystart);\n"
            f"    {expected_run_symbol}(rundot, clr);\n"
            "    label.llft(btex {\\sf E1} etex, wayhome+(-1,-2)) withcolor clr;\n"
            "    draw(firsthome) withcolor clr;\n\n"
        )

        assert at_bat.get_metapost_data(1) == expected_metapost

    @pytest.mark.parametrize(
        "end_base, metapost_play, draw_location",
        [
            (
                2,
                (
                    "    label.urt(btex {\\sf 1B} etex, waysecond) withcolor clr;\n"
                    "    label.urt(btex {\\sf 1} etex, waysecond+(0,10)) withcolor clr;\n"
                ),
                "firstsecond",
            ),
            (
                3,
                (
                    "    label.ulft(btex {\\sf 1B} etex, waythird) withcolor clr;\n"
                    "    label.ulft(btex {\\sf 1} etex, waythird+(0,10)) withcolor clr;\n"
                ),
                "firstthird",
            ),
        ],
    )
    def test_get_metapost_data_advance_as_runner(
        self, end_base, metapost_play, draw_location
    ):
        """Test that the get_metapost_data method is correct when the runner advances."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.last_base_reached = 1
        at_bat.advance(end_base, "1 1B")

        expected_metapost = (
            "    %% inning 1, batter 1\n"
            "    ystart := 1024;\n"
            "    set_vars(xstart,ystart);\n"
            f"{metapost_play}"
            f"    draw({draw_location}) withcolor clr;\n\n"
        )

        assert at_bat.get_metapost_data(1) == expected_metapost

    @pytest.mark.parametrize(
        "end_base, expected_run_symbol",
        [
            (4, "draw_dot"),
            ("U", "draw_cross"),
        ],
    )
    def test_get_metapost_data_advance_as_runner_score(
        self, end_base, expected_run_symbol
    ):
        """Test that the get_metapost_data method is correct when the runner advances and scores."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.last_base_reached = 1
        at_bat.advance(end_base, "1 1B")

        expected_metapost = (
            "    %% inning 1, batter 1\n"
            "    ystart := 1024;\n"
            "    set_vars(xstart,ystart);\n"
            f"    {expected_run_symbol}(rundot, clr);\n"
            "    label.lft(btex {\\sf 1} etex, wayhome+(-1,-2)) withcolor clr;\n"
            "    label.llft(btex {\\sf 1B} etex, wayhome+(-1,-5)) withcolor clr;\n"
            "    draw(firsthome) withcolor clr;\n\n"
        )

        assert at_bat.get_metapost_data(1) == expected_metapost

    @pytest.mark.parametrize(
        "start_base, end_base, metapost_data",
        [
            (
                1,
                1,
                {
                    "thrown_out_path": "cs_second",
                    "location": ".urt",
                    "label_loc": "waysecond",
                },
            ),
            (
                1,
                2,
                {
                    "thrown_out_path": "cs_second",
                    "location": ".urt",
                    "label_loc": "waysecond",
                },
            ),
            (
                1,
                3,
                {
                    "thrown_out_path": "cs_firstthird",
                    "location": ".ulft",
                    "label_loc": "waythird",
                },
            ),
            (
                1,
                4,
                {
                    "thrown_out_path": "to_firsthome",
                    "location": ".llft",
                    "label_loc": "wayhome+(-1,-2)",
                },
            ),
            (
                2,
                2,
                {
                    "thrown_out_path": "cs_third",
                    "location": ".ulft",
                    "label_loc": "waythird",
                },
            ),
            (
                2,
                3,
                {
                    "thrown_out_path": "cs_third",
                    "location": ".ulft",
                    "label_loc": "waythird",
                },
            ),
            (
                2,
                4,
                {
                    "thrown_out_path": "to_secondhome",
                    "location": ".llft",
                    "label_loc": "wayhome+(-1,-2)",
                },
            ),
            (
                3,
                3,
                {
                    "thrown_out_path": "to_home",
                    "location": ".llft",
                    "label_loc": "wayhome+(-1,-2)",
                },
            ),
            (
                3,
                4,
                {
                    "thrown_out_path": "to_home",
                    "location": ".llft",
                    "label_loc": "wayhome+(-1,-2)",
                },
            ),
        ],
    )
    def test_get_metapost_data_thrown_out_as_batter(
        self, start_base, end_base, metapost_data
    ):
        """Test that the get_metapost_data method is correct when the batter-runner is thrown out."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.last_base_reached = start_base
        at_bat.thrown_out(end_base, "9-4", 1)

        expected_metapost = (
            "    %% inning 1, batter 1\n"
            "    ystart := 1024;\n"
            "    set_vars(xstart,ystart);\n"
            f"    draw({metapost_data['thrown_out_path']}) withcolor outclr;\n"
            f"    label{metapost_data['location']}(btex {{\\sf 9-4}} etex, {metapost_data['label_loc']}) withcolor clr;\n"
            "    draw_out_one(xstart,ystart,clr);\n\n"
        )

        assert at_bat.get_metapost_data(1) == expected_metapost

    @pytest.mark.parametrize(
        "start_base, end_base, metapost_play, draw_location",
        [
            (
                1,
                1,
                (
                    "    label.urt(btex {\\sf FC4} etex, waysecond) withcolor clr;\n"
                    "    label.urt(btex {\\sf 1} etex, waysecond+(0,10)) withcolor clr;\n"
                ),
                "cs_second",
            ),
            (
                1,
                2,
                (
                    "    label.urt(btex {\\sf FC4} etex, waysecond) withcolor clr;\n"
                    "    label.urt(btex {\\sf 1} etex, waysecond+(0,10)) withcolor clr;\n"
                ),
                "cs_second",
            ),
            (
                1,
                3,
                (
                    "    label.ulft(btex {\\sf FC4} etex, waythird) withcolor clr;\n"
                    "    label.ulft(btex {\\sf 1} etex, waythird+(0,10)) withcolor clr;\n"
                ),
                "cs_firstthird",
            ),
            (
                1,
                4,
                (
                    "    label.lft(btex {\\sf 1} etex, wayhome+(-1,-2)) withcolor clr;\n"
                    "    label.llft(btex {\\sf FC4} etex, wayhome+(-1,-5)) withcolor clr;\n"
                ),
                "to_firsthome",
            ),
            (
                2,
                2,
                (
                    "    label.ulft(btex {\\sf FC4} etex, waythird) withcolor clr;\n"
                    "    label.ulft(btex {\\sf 1} etex, waythird+(0,10)) withcolor clr;\n"
                ),
                "cs_third",
            ),
            (
                2,
                3,
                (
                    "    label.ulft(btex {\\sf FC4} etex, waythird) withcolor clr;\n"
                    "    label.ulft(btex {\\sf 1} etex, waythird+(0,10)) withcolor clr;\n"
                ),
                "cs_third",
            ),
            (
                2,
                4,
                (
                    "    label.lft(btex {\\sf 1} etex, wayhome+(-1,-2)) withcolor clr;\n"
                    "    label.llft(btex {\\sf FC4} etex, wayhome+(-1,-5)) withcolor clr;\n"
                ),
                "to_secondhome",
            ),
            (
                3,
                3,
                (
                    "    label.lft(btex {\\sf 1} etex, wayhome+(-1,-2)) withcolor clr;\n"
                    "    label.llft(btex {\\sf FC4} etex, wayhome+(-1,-5)) withcolor clr;\n"
                ),
                "to_home",
            ),
            (
                3,
                4,
                (
                    "    label.lft(btex {\\sf 1} etex, wayhome+(-1,-2)) withcolor clr;\n"
                    "    label.llft(btex {\\sf FC4} etex, wayhome+(-1,-5)) withcolor clr;\n"
                ),
                "to_home",
            ),
        ],
    )
    def test_get_metapost_data_thrown_out_as_runner(
        self, start_base, end_base, metapost_play, draw_location
    ):
        """Test that the get_metapost_data method is correct when the runner is thrown out."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.last_base_reached = start_base
        at_bat.thrown_out(end_base, "1 FC4", 1)

        expected_metapost = (
            "    %% inning 1, batter 1\n"
            "    ystart := 1024;\n"
            "    set_vars(xstart,ystart);\n"
            f"    draw({draw_location}) withcolor outclr;\n"
            f"{metapost_play}"
            "    draw_out_one(xstart,ystart,clr);\n\n"
        )

        assert at_bat.get_metapost_data(1) == expected_metapost

    @pytest.mark.parametrize(
        "base, expected_metapost_loc, expected_metapost_base",
        [
            (1, ".rt", "first"),
            (2, ".top", "second"),
            (3, ".lft", "third"),
            (4, ".bot", "home"),
        ],
    )
    def test_get_metapost_data_atbase(
        self, base, expected_metapost_loc, expected_metapost_base
    ):
        """Test that the get_metapost_data method is correct on at-base labels."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.atbase("PR", base=base)

        expected_metapost = (
            "    %% inning 1, batter 1\n"
            "    ystart := 1024;\n"
            "    set_vars(xstart,ystart);\n"
            f"    label{expected_metapost_loc}(btex {{\\sf PR}} etex, {expected_metapost_base}) withcolor clr;\n\n"
        )
        assert at_bat.get_metapost_data(1) == expected_metapost

    def test_get_metapost_data_no_ab(self):
        """Test that the get_metapost_data method is correct when a batter's at-bat is not completed."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.no_ab("CS")

        expected_metapost = (
            "    %% inning 1, batter 1\n"
            "    ystart := 1024;\n"
            "    set_vars(xstart,ystart);\n"
            "    label(btex {\\bigsf CS} etex, outlabel) withcolor clr;\n\n"
        )
        assert at_bat.get_metapost_data(1) == expected_metapost

    def test_string_output_pitch_list(self):
        """Test that the string method is printing the expected format when the pitch_list method has been called."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.pitch_list("s s f f f f f f f f f f f f f f f f f f f f f b b b b")

        expected_str = (
            "1. #1 John Doe vs #2 Jack Doe\n"
            "Pitches: s s f f f f f f f f f f f f f f f f f f f f f b b b b\n\n"
        )
        assert str(at_bat) == expected_str

    def test_string_output_out(self):
        """Test that the string method is printing the expected format when an out is recorded for the batter."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.out("G3", 1)

        expected_str = (
            "1. #1 John Doe vs #2 Jack Doe\n" "Pitches: X\n" "    Out #1: G3\n" "\n"
        )

        assert str(at_bat) == expected_str

    @pytest.mark.parametrize(
        "hit, expected_advance",
        [
            (1, "    Advance (0 to 1): Hit on 1\n"),
            (2, "    Advance (0 to 2): Hit on 2\n"),
            (3, "    Advance (0 to 3): Hit on 3\n"),
            (4, "    Advance (0 to 4): Hit on 4\n"),
            ("U", "    Advance (0 to U): Hit on U\n"),
        ],
    )
    def test_string_output_hit(self, hit, expected_advance):
        """Test that the string method is printing the expected format when the batter gets a hit."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.hit(hit)

        expected_str = (
            "1. #1 John Doe vs #2 Jack Doe\n" "Pitches: H\n" f"{expected_advance}" "\n"
        )

        assert str(at_bat) == expected_str

    def test_string_output_reach(self):
        """Test that the string method is printing the expected format when the batter reaches base."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.reach("FC5")

        expected_str = (
            "1. #1 John Doe vs #2 Jack Doe\n"
            "Pitches: R\n"
            "    Advance (0 to 1): Reach on FC5\n"
            "\n"
        )

        assert str(at_bat) == expected_str

    def test_string_output_reach_error(self):
        """Test that the string method is printing the expected format when the batter reaches on an error."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.reach("E1")

        expected_str = (
            "1. #1 John Doe vs #2 Jack Doe\n"
            "Pitches: R\n"
            "    Advance (0 to 1): Error on E1\n"
            "\n"
        )

        assert str(at_bat) == expected_str

    def test_string_output_reach_strikeout(self):
        """Test that the string method is printing the expected format when the batter reaches on a strikeout."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.reach("K")

        expected_str = (
            "1. #1 John Doe vs #2 Jack Doe\n" "    Advance (0 to 1): Reach on K\n" "\n"
        )

        assert str(at_bat) == expected_str

    @pytest.mark.parametrize(
        "walk_type, expected_info",
        [
            ("BB", "Walk"),
            ("IBB", "Intent Walk"),
        ],
    )
    def test_string_output_reach_walk(self, walk_type, expected_info):
        """Test that the string method is printing the expected format when the batter reaches on a walk."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.reach(walk_type)

        expected_str = (
            "1. #1 John Doe vs #2 Jack Doe\n"
            f"    Advance (0 to 1): {expected_info} on {walk_type}\n"
            "\n"
        )

        assert str(at_bat) == expected_str

    @pytest.mark.parametrize(
        "end_base",
        [
            (2),
            (3),
            (4),
        ],
    )
    def test_string_output_advance_as_batter(self, end_base):
        """Test that the string method is printing the expected format when the batter-runner advances."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.last_base_reached = 1
        at_bat.advance(end_base, "1 1B")

        expected_str = (
            "1. #1 John Doe vs #2 Jack Doe\n"
            f"    Advance (1 to {end_base}): Advance on 1 1B\n"
            "\n"
        )

        assert str(at_bat) == expected_str

    @pytest.mark.parametrize(
        "start_base, end_base",
        [
            (1, 1),
            (1, 2),
            (1, 3),
            (1, 4),
            (2, 2),
            (2, 3),
            (2, 4),
            (3, 3),
            (3, 4),
        ],
    )
    def test_string_output_thrown_out_as_batter(self, start_base, end_base):
        """Test that the string method is printing the expected format when the batter-runner is thrown out."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.last_base_reached = start_base
        at_bat.thrown_out(end_base, "9-4", 1)

        expected_str = (
            "1. #1 John Doe vs #2 Jack Doe\n"
            f"    Out #1: Thrown out ({start_base} to {end_base}), 9-4\n"
            "\n"
        )

        assert str(at_bat) == expected_str

    @pytest.mark.parametrize(
        "base",
        [
            (1),
            (2),
            (3),
            (4),
        ],
    )
    def test_string_output_atbase(self, base):
        """Test that the string method is printing the expected format on at-base labels."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.atbase("PR", base=base)

        expected_str = (
            "1. #1 John Doe vs #2 Jack Doe\n" f"    Label at base {base}: PR\n" "\n"
        )
        assert str(at_bat) == expected_str

    def test_string_output_no_ab(self):
        """Test that the string method is printing the expected format when a batter's at-bat is not completed."""
        at_bat = AtBat(1, self._batter, self._pitcher, InningStats())
        at_bat.no_ab("CS")

        expected_str = "1. #1 John Doe vs #2 Jack Doe\n" "    No AB: CS\n" "\n"
        assert str(at_bat) == expected_str
