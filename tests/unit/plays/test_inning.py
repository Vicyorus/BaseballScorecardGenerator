import pytest
from baseball_scorecard.plays.inning import Inning
from baseball_scorecard.team.team import Team


class TestInning:
    """
    Tests the Inning class.

    Given the design choice of making most of the attributes of this class
    private, the unit testing possible with this module is minimal and
    conducted using the __str__ method for checking accuracy.

    For more in-depth testing, integration tests will be used.
    """

    @pytest.fixture(autouse=True)
    def setup_inning_data(self):
        self._away_team = Team(
            {
                "team": "Foo Bars",
                "roster": {
                    1: "John Doe",
                    2: "John Doe",
                    3: "John Doe",
                    4: "John Doe",
                    5: "John Doe",
                    6: "John Doe",
                    7: "John Doe",
                    8: "John Doe",
                    9: "John Doe",
                    10: "John Doe",
                    11: "John Doe",
                    12: "John Doe",
                    13: "John Doe",
                    14: "John Doe",
                    15: "John Doe",
                    16: "John Doe",
                    17: "John Doe",
                    18: "John Doe",
                    19: "John Doe",
                    20: "John Doe",
                },
                "starter": 1,
                "lefties": [1, 10, 11],
                "lineup": [
                    [1, "1"],
                    [2, "2"],
                    [3, "3"],
                    [4, "4"],
                    [5, "5"],
                    [6, "6"],
                    [7, "7"],
                    [8, "8"],
                    [9, "9"],
                ],
                "bench": [
                    [10, "C"],
                    [11, "1B"],
                    [12, "RF"],
                ],
                "bullpen": [13, 14, 15, 16, 17, 18, 19, 20],
            },
            False,
            True,
        )

        self._home_team = Team(
            {
                "team": "Bar Foos",
                "roster": {
                    1: "Jack Doe",
                    2: "Jack Doe",
                    3: "Jack Doe",
                    4: "Jack Doe",
                    5: "Jack Doe",
                    6: "Jack Doe",
                    7: "Jack Doe",
                    8: "Jack Doe",
                    9: "Jack Doe",
                    10: "Jack Doe",
                    11: "Jack Doe",
                    12: "Jack Doe",
                    13: "Jack Doe",
                    14: "Jack Doe",
                    15: "Jack Doe",
                    16: "Jack Doe",
                    17: "Jack Doe",
                    18: "Jack Doe",
                    19: "Jack Doe",
                    20: "Jack Doe",
                },
                "starter": 1,
                "lefties": [1, 10, 11],
                "lineup": [
                    [1, "1"],
                    [2, "2"],
                    [3, "3"],
                    [4, "4"],
                    [5, "5"],
                    [6, "6"],
                    [7, "7"],
                    [8, "8"],
                    [9, "9"],
                ],
                "bench": [
                    [10, "C"],
                    [11, "1B"],
                    [12, "RF"],
                ],
                "bullpen": [13, 14, 15, 16, 17, 18, 19, 20],
            },
            False,
            False,
        )

    def test_pitching_substitution(self):
        """Test that the pitching_substitution method is correct."""
        t1 = Inning(1, True, self._away_team, self._home_team)
        t1.pitching_substitution(10)
        t1.new_ab()

        expected_str = (
            "Top of the 1st\n"
            "Pitching substitution: #10 Jack Doe\n"
            "1. #1 John Doe vs #10 Jack Doe\n\n"
            "Inning totals:\n\n"
        )

        assert str(t1) == expected_str

    def test_offensive_substitution_pinch_hitter(self):
        """Test that the offensive_substitution method is correct for a pinch-hitter."""
        t1 = Inning(1, True, self._away_team, self._home_team)
        t1.offensive_substitution(1, 10, "PH")
        t1.new_ab()

        expected_str = (
            "Top of the 1st\n"
            "Offensive substitution (Pinch-hitter): #10 John Doe\n"
            "1. #10 John Doe vs #1 Jack Doe\n\n"
            "Inning totals:\n\n"
        )

        assert str(t1) == expected_str

    def test_offensive_substitution_pinch_hitter(self):
        """Test that the offensive_substitution method is correct for a pinch-runner."""
        t1 = Inning(1, True, self._away_team, self._home_team)
        t1.new_ab()
        t1.hit(1)
        t1.offensive_substitution(1, 10, "PR")

        expected_str = (
            "Top of the 1st\n"
            "1. #1 John Doe vs #1 Jack Doe\n"
            "Pitches: H\n"
            "    Advance (0 to 1): Hit on 1\n\n"
            "Offensive substitution (Pinch-runner): #10 John Doe\n"
            "Inning totals: 1 H 1 LOB 1 P 1 S\n\n"
        )

        assert str(t1) == expected_str

    def test_defensive_substitution_home_team(self):
        """Test that the defensive_substitution method is correct for the home team."""
        t1 = Inning(1, True, self._away_team, self._home_team)
        t1.defensive_substitution(1, 10, "1")

        b1 = Inning(1, False, self._away_team, self._home_team)

        expected_t1_str = (
            "Top of the 1st\n"
            "Defensive substitution: #10 Jack Doe\n"
            "Inning totals:\n\n"
        )
        expected_b1_str = "Bottom of the 1st\n" "Inning totals:\n\n"

        assert str(t1) == expected_t1_str
        assert str(b1) == expected_b1_str

    def test_defensive_substitution_away_team(self):
        """Test that the defensive_substitution method is correct for the away team."""
        b1 = Inning(1, False, self._away_team, self._home_team)
        b1.defensive_substitution(1, 10, "1")

        t2 = Inning(2, True, self._away_team, self._home_team)

        expected_b1_str = (
            "Bottom of the 1st\n"
            "Defensive substitution: #10 John Doe\n"
            "Inning totals:\n\n"
        )
        expected_t2_str = "Top of the 2nd\n" "Inning totals:\n\n"

        assert str(b1) == expected_b1_str
        assert str(t2) == expected_t2_str

    def test_pitch_list(self):
        """Test that the pitch_list method is correct."""
        inning = Inning(1, True, self._away_team, self._home_team)
        inning.new_ab()
        inning.pitch_list("c c c")

        expected_str = (
            "Top of the 1st\n"
            "1. #1 John Doe vs #1 Jack Doe\n"
            "Pitches: c c c\n\n"
            "Inning totals: 3 P 3 S\n\n"
        )
        assert str(inning) == expected_str

    def test_out(self):
        """Test that the out method is correct."""
        inning = Inning(1, True, self._away_team, self._home_team)
        inning.new_ab()
        inning.out("G3", 1)

        expected_str = (
            "Top of the 1st\n"
            "1. #1 John Doe vs #1 Jack Doe\n"
            "Pitches: X\n"
            "    Out #1: G3\n\n"
            "Inning totals: 1 P 1 S\n\n"
        )
        assert str(inning) == expected_str

    def test_out_exception_raised_too_many_outs(self):
        """Test that the out method raises an exception when more than 3 outs are attempted in an inning."""
        inning = Inning(1, True, self._away_team, self._home_team)
        inning.new_ab()
        inning.out("G3", 1)

        inning.new_ab()
        inning.out("G3", 1)

        inning.new_ab()
        inning.out("G3", 1)

        inning.new_ab()
        with pytest.raises(Exception):
            inning.out("G3", 1)

    def test_out_strikeout(self):
        """Test that the out method is correct."""
        inning = Inning(1, True, self._away_team, self._home_team)
        inning.new_ab()
        inning.out("K", 1)

        expected_str = (
            "Top of the 1st\n"
            "1. #1 John Doe vs #1 Jack Doe\n"
            "    Out #1: K\n\n"
            "Inning totals: 1 K\n\n"
        )
        assert str(inning) == expected_str

    def test_hit(self):
        """Test that the hit method is correct."""
        inning = Inning(1, True, self._away_team, self._home_team)
        inning.new_ab()
        inning.hit(1)

        expected_str = (
            "Top of the 1st\n"
            "1. #1 John Doe vs #1 Jack Doe\n"
            "Pitches: H\n"
            "    Advance (0 to 1): Hit on 1\n\n"
            "Inning totals: 1 H 1 LOB 1 P 1 S\n\n"
        )
        assert str(inning) == expected_str

    def test_hit_homerun(self):
        """Test that the hit method is correct, when a player hits a home run."""
        inning = Inning(1, True, self._away_team, self._home_team)
        inning.new_ab()
        inning.hit(4)

        expected_str = (
            "Top of the 1st\n"
            "1. #1 John Doe vs #1 Jack Doe\n"
            "Pitches: H\n"
            "    Advance (0 to 4): Hit on 4\n\n"
            "Inning totals: 1 R 1 H 1 P 1 S\n\n"
        )
        assert str(inning) == expected_str

    def test_reach(self):
        """Test that the reach method is correct."""
        inning = Inning(1, True, self._away_team, self._home_team)
        inning.new_ab()
        inning.reach("FC5")

        expected_str = (
            "Top of the 1st\n"
            "1. #1 John Doe vs #1 Jack Doe\n"
            "Pitches: R\n"
            "    Advance (0 to 1): Reach on FC5\n\n"
            "Inning totals: 1 LOB 1 P 1 S\n\n"
        )
        assert str(inning) == expected_str

    def test_reach_error(self):
        """Test that the reach method is correct, when a batter reaches on an error."""
        inning = Inning(1, True, self._away_team, self._home_team)
        inning.new_ab()
        inning.reach("E1")

        expected_str = (
            "Top of the 1st\n"
            "1. #1 John Doe vs #1 Jack Doe\n"
            "Pitches: R\n"
            "    Advance (0 to 1): Error on E1\n\n"
            "Inning totals: 1 LOB 1 P 1 S\n\n"
        )
        assert str(inning) == expected_str

    def test_reach_strikeout(self):
        """Test that the reach method is correct, when a batter reaches on a strikeout."""
        inning = Inning(1, True, self._away_team, self._home_team)
        inning.new_ab()
        inning.reach("K")

        expected_str = (
            "Top of the 1st\n"
            "1. #1 John Doe vs #1 Jack Doe\n"
            "    Advance (0 to 1): Reach on K\n\n"
            "Inning totals: 1 LOB 1 K\n\n"
        )
        assert str(inning) == expected_str

    def test_advance(self):
        """Test that the advance method is correct."""
        inning = Inning(1, True, self._away_team, self._home_team)

        # 1. Jack Doe
        inning.new_ab()
        inning.hit(1)
        inning.advance(2, "2 SB")

        # 2. Jack Doe
        inning.new_ab()
        inning.hit(1)

        expected_str = (
            "Top of the 1st\n"
            "1. #1 John Doe vs #1 Jack Doe\n"
            "Pitches: H\n"
            "    Advance (0 to 1): Hit on 1\n"
            "    Advance (1 to 2): Advance on 2 SB\n\n"
            "2. #2 John Doe vs #1 Jack Doe\n"
            "Pitches: H\n"
            "    Advance (0 to 1): Hit on 1\n\n"
            "Inning totals: 2 H 2 LOB 2 P 2 S\n\n"
        )
        assert str(inning) == expected_str

    def test_advance_score(self):
        """Test that the advance method is correct, when a batter advances and scores."""
        inning = Inning(1, True, self._away_team, self._home_team)
        # 1. John Doe
        inning.new_ab()
        inning.hit(1)
        inning.advance(4, "2 3B")

        # 2. John Doe
        inning.new_ab()
        inning.hit(3, rbis=1)

        expected_str = (
            "Top of the 1st\n"
            "1. #1 John Doe vs #1 Jack Doe\n"
            "Pitches: H\n"
            "    Advance (0 to 1): Hit on 1\n"
            "    Advance (1 to 4): Advance on 2 3B\n\n"
            "2. #2 John Doe vs #1 Jack Doe\n"
            "Pitches: H\n"
            "    Advance (0 to 3): Hit on 3\n\n"
            "Inning totals: 1 R 2 H 1 LOB 2 P 2 S\n\n"
        )
        assert str(inning) == expected_str

    def test_thrown_out(self):
        """Test that the thrown_out method is correct."""
        inning = Inning(1, True, self._away_team, self._home_team)
        # 1. John Doe
        inning.new_ab()
        inning.hit(1)
        inning.thrown_out(2, "2 POCS")

        # 2. John Doe
        inning.new_ab()
        inning.reach("HBP")

        expected_str = (
            "Top of the 1st\n"
            "1. #1 John Doe vs #1 Jack Doe\n"
            "Pitches: H\n"
            "    Advance (0 to 1): Hit on 1\n"
            "    Out #1: Thrown out (1 to 2), 2 POCS\n\n"
            "2. #2 John Doe vs #1 Jack Doe\n"
            "Pitches: R\n"
            "    Advance (0 to 1): Hit By Pitch on HBP\n\n"
            "Inning totals: 1 H 1 LOB 2 P 1 S\n\n"
        )
        assert str(inning) == expected_str

    def test_thrown_out_non_default_out(self):
        """Test that the thrown_out method is correct, when specifying the out number."""
        inning = Inning(1, True, self._away_team, self._home_team)
        # 1. John Doe
        inning.new_ab()
        inning.hit(1)
        inning.thrown_out(2, "2 DP3", out_number=2)

        # 2. John Doe
        inning.new_ab()
        inning.out("DP3")

        expected_str = (
            "Top of the 1st\n"
            "1. #1 John Doe vs #1 Jack Doe\n"
            "Pitches: H\n"
            "    Advance (0 to 1): Hit on 1\n"
            "    Out #2: Thrown out (1 to 2), 2 DP3\n\n"
            "2. #2 John Doe vs #1 Jack Doe\n"
            "Pitches: X\n"
            "    Out #1: DP3\n\n"
            "Inning totals: 1 H 2 P 2 S\n\n"
        )
        assert str(inning) == expected_str

    def test_thrown_out_different_pitcher(self):
        """Test that the thrown_out method is correct, when specifying the pitcher."""
        inning = Inning(1, True, self._away_team, self._home_team)
        # 1. John Doe
        inning.new_ab()
        inning.hit(1)
        inning.thrown_out(2, "2 DP3", out_number=2, pitcher_id=10)

        # Pitching substitution
        inning.pitching_substitution(10)

        # 2. John Doe
        inning.new_ab()
        inning.out("DP3")

        expected_str = (
            "Top of the 1st\n"
            "1. #1 John Doe vs #1 Jack Doe\n"
            "Pitches: H\n"
            "    Advance (0 to 1): Hit on 1\n"
            "    Out #2: Thrown out (1 to 2), 2 DP3\n\n"
            "Pitching substitution: #10 Jack Doe\n"
            "2. #2 John Doe vs #10 Jack Doe\n"
            "Pitches: X\n"
            "    Out #1: DP3\n\n"
            "Inning totals: 1 H 2 P 2 S\n\n"
        )
        assert str(inning) == expected_str

    def test_thrown_out_exception_raised_out_reused(self):
        """Test that the thrown_out method raises an exception when an out is attempted to be reused."""
        inning = Inning(1, True, self._away_team, self._home_team)
        # 1. John Doe
        inning.new_ab()
        inning.out("G3")

        # 2. John Doe
        inning.new_ab()
        inning.hit(1)
        with pytest.raises(Exception):
            inning.thrown_out(2, "2 DP3", out_number=1)

    def test_thrown_out_exception_raised_too_many_outs(self):
        """Test that the thrown_out method raises an exception when more than 3 outs are attempted on the same inning."""
        inning = Inning(1, True, self._away_team, self._home_team)
        # 1. John Doe
        inning.new_ab()
        inning.out("G3")

        inning.new_ab()
        inning.out("G3")

        inning.new_ab()
        inning.out("G3")

        inning.new_ab()
        inning.hit(1)
        with pytest.raises(Exception):
            inning.thrown_out(2, "2 DP3")

    def test_place_runner(self):
        """Test that the thrown_out method is correct."""
        inning = Inning(1, True, self._away_team, self._home_team)
        # 9. John Doe
        inning.place_runner()

        expected_str = (
            "Top of the 1st\n"
            "9. #9 John Doe vs #1 Jack Doe\n"
            "Pitches: R\n"
            "    Advance (0 to 2): Reach on RP\n"
            "    Label at base 2: RP\n\n"
            "Inning totals: 1 LOB 1 P 1 S\n\n"
        )
        assert str(inning) == expected_str

    def test_place_runner_specific_player(self):
        """Test that the thrown_out method is correct, for a specific player."""
        inning = Inning(1, True, self._away_team, self._home_team)
        # 9. John Doe
        inning.place_runner(2)

        expected_str = (
            "Top of the 1st\n"
            "2. #2 John Doe vs #1 Jack Doe\n"
            "Pitches: R\n"
            "    Advance (0 to 2): Reach on RP\n"
            "    Label at base 2: RP\n\n"
            "Inning totals: 1 LOB 1 P 1 S\n\n"
        )
        assert str(inning) == expected_str

    def test_error(self):
        """Test that the error method is correct."""
        inning = Inning(1, True, self._away_team, self._home_team)
        inning.error(1)

        expected_str = "Top of the 1st\n" "Inning totals: 1 E\n\n"
        assert str(inning) == expected_str

    def test_atbase(self):
        """Test that the atbase method is correct."""
        inning = Inning(1, True, self._away_team, self._home_team)
        inning.new_ab()
        inning.hit(1)
        inning.atbase("PR")

        expected_str = (
            "Top of the 1st\n"
            "1. #1 John Doe vs #1 Jack Doe\n"
            "Pitches: H\n"
            "    Advance (0 to 1): Hit on 1\n"
            "    Label at base 1: PR\n\n"
            "Inning totals: 1 H 1 LOB 1 P 1 S\n\n"
        )
        assert str(inning) == expected_str

    def test_no_ab(self):
        """Test that the no_ab method is correct."""
        inning = Inning(1, True, self._away_team, self._home_team)
        inning.new_ab()
        inning.no_ab("CS")

        expected_str = (
            "Top of the 1st\n"
            "1. #1 John Doe vs #1 Jack Doe\n"
            "    No AB: CS\n\n"
            "Inning totals:\n\n"
        )
        assert str(inning) == expected_str

    def test_inning_ordinal_naming(self):
        """Test that the correct ordinal number is printed for the label at the start of the inning."""

        inning_cardinal_ordinal_mapping = {
            1: "1st",
            2: "2nd",
            3: "3rd",
            4: "4th",
            5: "5th",
            6: "6th",
            7: "7th",
            8: "8th",
            9: "9th",
            10: "10th",
            11: "11th",
            12: "12th",
            13: "13th",
            14: "14th",
            15: "15th",
            16: "16th",
            17: "17th",
            18: "18th",
            19: "19th",
            20: "20th",
            21: "21st",
            22: "22nd",
            23: "23rd",
            24: "24th",
        }

        for k, v in inning_cardinal_ordinal_mapping.items():
            inning = Inning(
                k,
                True,
                self._away_team,
                self._home_team,
            )

            expected_str = f"Top of the {v}\n" "Inning totals:\n\n"
            assert str(inning) == expected_str
