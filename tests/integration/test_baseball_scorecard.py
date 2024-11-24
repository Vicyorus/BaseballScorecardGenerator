import filecmp
import os
import pytest
from baseball_scorecard.baseball_scorecard import Scorecard
from .expected_results.string_result import EXPECTED_STR_RESULT


class TestBaseballScorecard:
    """Integration tests for the baseball_scorecard module.

    This tests all the public functions for both the Scorecard and Inning classes.
    """

    @pytest.fixture(autouse=True)
    def setup_game_data(self):
        self._game_data = {
            "scorer": "Sco Rer",
            "date": "1970-01-01 10:00-13:00",
            "at": "Testname Park, Cityville",
            "att": "45,000",
            "temp": "78F, Sunny",
            "wind": "10mph, Out To RF",
            "away": {
                "team": "Foo Bars",
                "starter": 1,
                "roster": {
                    # Lineup
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
                },
                "lefties": [1],
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
                    [11, "1B"],
                    [12, "CF"],
                    [13, "C"],
                ],
                "bullpen": [10],
            },
            "home": {
                "team": "Bar Foos",
                "starter": 21,
                "roster": {
                    # Lineup
                    21: "Jack Doe",
                    22: "Jack Doe",
                    23: "Jack Doe",
                    24: "Jack Doe",
                    25: "Jack Doe",
                    26: "Jack Doe",
                    27: "Jack Doe",
                    28: "Jack Doe",
                    29: "Jack Doe",
                    30: "Jack Doe",
                    31: "Jack Doe",
                    32: "Jack Doe",
                    33: "Jack Doe",
                },
                "lefties": [21],
                "lineup": [
                    [21, "1"],
                    [22, "2"],
                    [23, "3"],
                    [24, "4"],
                    [25, "5"],
                    [26, "6"],
                    [27, "7"],
                    [28, "8"],
                    [29, "9"],
                ],
                "bench": [
                    [31, "2B"],
                    [32, "RF"],
                    [33, "C"],
                ],
                "bullpen": [30],
            },
            "umpires": {
                "HP": "HP Umpire",
                "1B": "1B Umpire",
                "2B": "2B Umpire",
                "3B": "3B Umpire",
            },
        }

    def _write_empty_templates(self, tmp_path):
        """Helper function to write empty Metapost/LaTeX templates."""
        team_template = tmp_path / "team_scorecard_template.mp"
        team_template.write_text("")
        final_template = tmp_path / "final_scorecard_template.tex"
        final_template.write_text("")

    def _nine_inning_game_calls(self, scorecard: Scorecard):
        """Helper function that runs a 9-inning game. Based in the 2024-07-29 SEA @ BOS game."""

        ##########################################################
        # 1st Inning
        ##########################################################
        # Top 1st
        t1 = scorecard.new_inning()

        # 1. FOO #1 John Doe
        t1.new_ab()
        t1.pitch_list("s")
        t1.out("L9")

        # 2. FOO #2 John Doe
        t1.new_ab()
        t1.pitch_list("b c b c f c")
        t1.out("!K")

        # 3. FOO #3 John Doe
        t1.new_ab()
        t1.pitch_list("s c b b b s")
        t1.out("K")

        # Bot 1st
        b1 = scorecard.new_inning()

        # 1. BAR #21 Jack Doe
        b1.new_ab()
        b1.pitch_list("f f b f s")
        b1.out("K")

        # 2. BAR #22 Jack Doe
        b1.new_ab()
        b1.pitch_list("c b s b s")
        b1.out("K")

        # 3. BAR #23 Jack Doe
        b1.new_ab()
        b1.pitch_list("c")
        b1.out("G3-1")

        ##########################################################
        # 2nd Inning
        ##########################################################
        # Top 2nd
        t2 = scorecard.new_inning()

        # 4. FOO #4 John Doe
        t2.new_ab()
        t2.pitch_list("b b b c c")
        t2.hit(1)
        t2.advance(2, "5 BLK")
        t2.thrown_out(3, "6 TP5-4-3", 1, 21)

        # 5. FOO #5 John Doe
        t2.new_ab(is_risp=True)
        t2.pitch_list("c")
        t2.balk()
        t2.hit(1)
        t2.thrown_out(2, "6 TP5-4-3", 2, 21)

        # 6. FOO #6 John Doe
        t2.new_ab(is_risp=True)
        t2.pitch_list("f t b s")
        t2.out("TP5-4-3")

        # Bot 2nd
        b2 = scorecard.new_inning()

        # 4. BAR #24 Jack Doe
        b2.new_ab()
        b2.pitch_list("b s b")
        b2.out("G3-1")

        # 5. BAR #25 Jack Doe
        b2.new_ab()
        b2.pitch_list("b t b c b")
        b2.out("L7")

        # 6. BAR #26 Jack Doe
        b2.new_ab()
        b2.pitch_list("c s b s")
        b2.out("K")

        ##########################################################
        # 3rd Inning
        ##########################################################
        # Top 3rd
        t3 = scorecard.new_inning()

        # 7. FOO #7 John Doe
        t3.new_ab()
        t3.pitch_list("c f b s")
        t3.out("K")

        # 8. FOO #8 John Doe
        t3.new_ab()
        t3.pitch_list("c b")
        t3.hit(1)
        t3.advance(2, "9 1B")

        # 9. FOO #9 John Doe
        t3.new_ab()
        t3.pitch_list("b 1 b")
        t3.hit(1)
        t3.thrown_out(2, "1 DP5-4-3", 2, 21)

        # 1. FOO #1 John Doe
        t3.new_ab(is_risp=True)
        t3.pitch_list("f")
        t3.out("DP5-4-3")

        # Bot 3rd
        b3 = scorecard.new_inning()

        # 7. BAR #27 Jack Doe
        b3.new_ab()
        b3.pitch_list("c b f")
        b3.hit(1)
        b3.advance(2, "29 1B")
        b3.advance(3, "21 FC1-6")
        b3.advance(4, "22 WP")

        # 8. BAR #28 Jack Doe
        b3.new_ab()
        b3.pitch_list("c b b f c")
        b3.out("!K")

        # 9. BAR #29 Jack Doe
        b3.new_ab()
        b3.pitch_list("s d s 1")
        b3.hit(1)
        b3.thrown_out(2, "21 FC1-6", 2, 1)

        # 1. BAR #21 Jack Doe
        b3.new_ab(is_risp=True)
        b3.pitch_list("f b d s f")
        b3.reach("FC1-6")
        b3.advance(2, "22 SB")
        b3.advance(3, "22 WP")
        b3.advance(4, "22 1B")

        # 2. BAR #22 Jack Doe
        b3.new_ab(is_risp=True)
        b3.pitch_list("s s f b b b f pso f f f f")
        b3.wp()
        b3.hit(1, rbis=1)
        b3.advance(4, "23 HR")

        # 3. BAR #23 Jack Doe
        b3.new_ab()
        b3.hit(4, rbis=2)

        # 4. BAR #24 Jack Doe
        b3.new_ab()
        b3.pitch_list("c b s")
        b3.hit(2)
        b3.advance(4, "25 2B")

        # 5. BAR #25 Jack Doe
        b3.new_ab(is_risp=True)
        b3.hit(2, rbis=1)
        b3.advance(4, "26 2B")

        # 6. BAR #26 Jack Doe
        b3.new_ab(is_risp=True)
        b3.pitch_list("b s d c b")
        b3.hit(2, rbis=1)
        b3.advance(3, "27 PB")
        b3.advance(4, "27 2B")

        # 7. BAR #27 Jack Doe
        b3.new_ab(is_risp=True)
        b3.pitch_list("b")
        b3.pb()
        b3.hit(2, rbis=1)
        b3.thrown_out(3, "28 CS", 3, 1)

        # 8. BAR #28 Jack Doe
        b3.new_ab(is_risp=True)
        b3.pitch_list("c")
        b3.no_ab("CS")

        ##########################################################
        # 4th Inning
        ##########################################################
        # Top 4th
        t4 = scorecard.new_inning()

        # 2. FOO #2 John Doe
        t4.new_ab()
        t4.pitch_list("c")
        t4.hit(2)
        t4.advance(3, "3 SAC1-3")
        t4.advance(4, "4 SF7")

        # 3. FOO #3 John Doe
        t4.new_ab(is_risp=True)
        t4.pitch_list("b")
        t4.out("SAC1-3")

        # 4. FOO #4 John Doe
        t4.new_ab(is_risp=True)
        t4.out("SF7", rbis=1)

        # 5. FOO #5 John Doe
        t4.new_ab()
        t4.pitch_list("c s b s")
        t4.out("K")

        # Bot 4th
        b4 = scorecard.new_inning()

        # 8. BAR #28 Jack Doe
        b4.new_ab()
        b4.pitch_list("b b c s")
        b4.out("G6-3")

        # 9. BAR #29 Jack Doe
        b4.new_ab()
        b4.hit(1)
        b4.advance(3, "21 2B")
        b4.advance(4, "22 2B")

        # 1. BAR #21 Jack Doe
        b4.new_ab()
        b4.pitch_list("1 f b")
        b4.hit(2)
        b4.advance(3, "22 2B")
        b4.advance(4, "23 1B")

        # 2. BAR #22 Jack Doe
        b4.new_ab(is_risp=True)
        b4.pitch_list("b")
        b4.hit(2, rbis=1)
        b4.advance(4, "23 1B")

        # 3. BAR #23 Jack Doe
        b4.new_ab(is_risp=True)
        b4.pitch_list("c b b")
        b4.hit(1, rbis=2)

        # 4. BAR #24 Jack Doe
        b4.new_ab()
        b4.pitch_list("b b")
        b4.out("(F)P5")

        # 5. BAR #25 Jack Doe
        b4.new_ab()
        b4.pitch_list("c s")
        b4.out("F9")

        ##########################################################
        # 5th Inning
        ##########################################################
        # Top 5th
        t5 = scorecard.new_inning()

        # 6. FOO #6 John Doe
        t5.new_ab()
        t5.pitch_list("c b f b")
        t5.out("F8")

        # 7. FOO #7 John Doe
        t5.new_ab()
        t5.pitch_list("f f b b f")
        t5.hit(1)

        # 8. FOO #8 John Doe
        t5.new_ab()
        t5.pitch_list("c f b b c")
        t5.out("!K")

        # 9. FOO #9 John Doe
        t5.new_ab()
        t5.pitch_list("c b s b b s")
        t5.out("K")

        # Bot 5th
        b5 = scorecard.new_inning()

        # 6. BAR #26 Jack Doe
        b5.new_ab()
        b5.pitch_list("c")
        b5.hit(4)

        # 7. BAR #27 Jack Doe
        b5.new_ab()
        b5.pitch_list("b f t f b f c")
        b5.out("!K")

        # 8. BAR #28 Jack Doe
        b5.new_ab()
        b5.pitch_list("f b")
        b5.out("F8")

        # 9. BAR #29 Jack Doe
        b5.new_ab()
        b5.pitch_list("c c")
        b5.error(4)
        b5.reach("E4", 2)
        b5.advance(3, "21 SB")
        b5.advance("U", "21 SF7")

        # 1. BAR #21 Jack Doe
        b5.new_ab(is_risp=True)
        b5.pitch_list("f b")
        b5.error(7)
        b5.reach("SF7")

        # 2. BAR #22 Jack Doe
        b5.new_ab(is_risp=True)
        b5.pitch_list("c f b d b s")
        b5.out("K")

        ##########################################################
        # 6th Inning
        ##########################################################
        # Top 6th
        t6 = scorecard.new_inning()

        # 1. FOO #1 John Doe
        t6.new_ab()
        t6.pitch_list("c f b s")
        t6.out("K")

        # 2. FOO #2 John Doe
        t6.new_ab()
        t6.pitch_list("b b c")
        t6.hit(4)

        # 3. FOO #3 John Doe
        t6.new_ab()
        t6.pitch_list("c s b")
        t6.hit(4)

        # 4. FOO #4 John Doe
        t6.new_ab()
        t6.pitch_list("f b f b s")
        t6.out("K")

        # 5. FOO #5 John Doe
        t6.new_ab()
        t6.pitch_list("f")
        t6.out("L6")

        # Bot 6th
        b6 = scorecard.new_inning()

        # Pitching change for away team.
        b6.pitching_substitution(10)

        # Defensive change for away team.
        b6.defensive_substitution(4, 11, "4")

        # 3. BAR #23 Jack Doe
        b6.new_ab()
        b6.hit(2)
        b6.advance(4, "31 HR")

        # Offensive change for home team.
        b6.offensive_substitution(4, 31, "PH")

        # 4. BAR #31 Jack Doe
        b6.new_ab(is_risp=True)
        b6.pitch_list("b")
        b6.hit(4, rbis=2)

        # 5. BAR #25 Jack Doe
        b6.new_ab()
        b6.pitch_list("c f b b f b s")
        b6.out("K")

        # 6. BAR #26 Jack Doe
        b6.new_ab()
        b6.pitch_list("c c b s")
        b6.out("K")

        # 7. BAR #27 Jack Doe
        b6.new_ab()
        b6.pitch_list("f c b b f b")
        b6.out("L7")

        ##########################################################
        # 7th Inning
        ##########################################################
        # Top 7th
        t7 = scorecard.new_inning()

        # Defensive switch for home team pinch-hitter.
        t7.defensive_switch(31, "4")

        # 6. FOO #6 John Doe
        t7.new_ab()
        t7.pitch_list("ab f pv f")
        t7.error(5)
        t7.reach("E5", 2)
        t7.advance(3, "9 DI")
        t7.advance(4, "1 SAC1")

        # 7. FOO #7 John Doe
        t7.new_ab()
        t7.pitch_list("c f f s")
        t7.out("K")

        # 8. FOO #8 John Doe
        t7.new_ab()
        t7.pitch_list("c b b b s f pso")
        t7.out("(F)P5")

        # 9. FOO #9 John Doe
        t7.new_ab(is_risp=True)
        t7.pitch_list("d b b c b")
        t7.reach("BB")

        # 1. FOO #1 John Doe
        t7.new_ab(is_risp=True)
        t7.pitch_list("f f b b")
        t7.error(1)
        t7.reach("SAC1")
        t7.thrown_out(2, "1-4", 3, 21)

        # Bot 7th
        b7 = scorecard.new_inning()

        # 8. BAR #28 Jack Doe
        b7.new_ab()
        b7.pitch_list("f b b c")
        b7.out("G3-1")

        # 9. BAR #29 Jack Doe
        b7.new_ab()
        b7.pitch_list("s")
        b7.out("(F)P3")

        # 1. BAR #21 Jack Doe
        b7.new_ab()
        b7.pitch_list("b c b c b f t")
        b7.out("KT")

        ##########################################################
        # 8th Inning
        ##########################################################
        # Top 8th
        t8 = scorecard.new_inning()

        # 2. FOO #2 John Doe
        t8.new_ab()
        t8.pitch_list("f b b s f c")
        t8.out("!K")

        # 3. FOO #3 John Doe
        t8.new_ab()
        t8.pitch_list("s b s b f b")
        t8.hit(1)
        t8.advance(2, "11 1B")
        t8.advance(3, "5 BB")
        t8.advance(4, "6 2B")

        # 4. FOO #11 John Doe
        t8.new_ab()
        t8.hit(1)
        t8.advance(2, "5 BB")
        t8.advance(4, "6 2B")

        # 5. FOO #5 John Doe
        t8.new_ab(is_risp=True)
        t8.pitch_list("b d b c b")
        t8.reach("BB")
        t8.advance(3, "6 2B")
        t8.advance(4, "7 WP")

        # 6. FOO #6 John Doe
        t8.new_ab(is_risp=True)
        t8.pitch_list("b")
        t8.hit(2, rbis=2)
        t8.advance(3, "7 WP")
        t8.advance(4, "7 G4-3")

        # 7. FOO #7 John Doe
        t8.new_ab()
        t8.pitch_list("s s b")
        t8.wp()
        t8.out("G4-3", rbis=1)

        # 8. FOO #8 John Doe
        t8.new_ab()
        t8.pitch_list("f b b s b s")
        t8.out("K")

        # Bot 8th
        b8 = scorecard.new_inning()

        # 2. BAR #22 Jack Doe
        b8.new_ab()
        b8.pitch_list("c")
        b8.out("P6")

        # 3. BAR #23 Jack Doe
        b8.new_ab()
        b8.out("G4-3")

        # 4. BAR #31 Jack Doe
        b8.new_ab()
        b8.pitch_list("c b b b b")
        b8.reach("BB")

        # 5. BAR #25 Jack Doe
        b8.new_ab()
        b8.out("G4-3")

        ##########################################################
        # 9th Inning
        ##########################################################
        # Top 9th
        t9 = scorecard.new_inning()

        # Pitching change for home team.
        t9.pitching_substitution(30)

        # 9. FOO #9 John Doe
        t9.new_ab()
        t9.hit(1)

        # 1. FOO #1 John Doe
        t9.new_ab()
        t9.pitch_list("s c c")
        t9.out("!K")

        # 2. FOO #2 John Doe
        t9.new_ab()
        t9.pitch_list("s")
        t9.out("F7")

        # 3. FOO #3 John Doe
        t9.new_ab()
        t9.out("(F)P5")

        # Winning team: BAR
        # WP: BAR #21 Jack Doe
        scorecard.winning_pitcher(21)

        # SV: BAR #30 Jack Doe
        scorecard.save_pitcher(30)

        # Loser team: FOO
        # LP: FOO #1 John Doe
        scorecard.losing_pitcher(1, is_away_team=True)

    def test_baseball_scorecard_empty_scorecard(self, tmp_path):
        """Tests the scenario where an empty scorecard is generated."""

        self._write_empty_templates(tmp_path)

        expected_results_folder = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "expected_results",
            "empty_scorecard",
        )

        scorecard = Scorecard(
            output_dir=tmp_path,
            template_dir=tmp_path,
            data=self._game_data,
        )

        scorecard.generate_scorecard()

        assert filecmp.cmp(
            os.path.join(expected_results_folder, "scorecard_home.mp"),
            tmp_path / "scorecard_home.mp",
        )

        assert filecmp.cmp(
            os.path.join(expected_results_folder, "scorecard_away.mp"),
            tmp_path / "scorecard_away.mp",
        )

    def test_baseball_scorecard_home_team_win_save_away_team_lose(self, tmp_path):
        """
        Tests the scenario for the home team winning and getting a save,
        and the away team getting the loss.
        """

        self._write_empty_templates(tmp_path)

        expected_results_folder = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "expected_results",
            "home_win",
        )

        scorecard = Scorecard(
            output_dir=tmp_path,
            template_dir=tmp_path,
            data=self._game_data,
        )

        # Register the save pitcher
        scorecard.new_inning().pitching_substitution(30)

        # Winning team: BAR
        # WP: BAR #21 Jack Doe
        scorecard.winning_pitcher(21)

        # SV: BAR #30 Jack Doe
        scorecard.save_pitcher(30)

        # Loser team: FOO
        # LP: FOO #1 John Doe
        scorecard.losing_pitcher(1, is_away_team=True)

        scorecard.generate_scorecard()

        assert filecmp.cmp(
            os.path.join(expected_results_folder, "scorecard_home.mp"),
            tmp_path / "scorecard_home.mp",
        )

        assert filecmp.cmp(
            os.path.join(expected_results_folder, "scorecard_away.mp"),
            tmp_path / "scorecard_away.mp",
        )

    def test_baseball_scorecard_away_team_win_save_home_team_lose(self, tmp_path):
        """
        Tests the scenario for the away team winning and getting a save,
        and the home team getting the loss.
        """

        self._write_empty_templates(tmp_path)

        expected_results_folder = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "expected_results",
            "away_win",
        )

        scorecard = Scorecard(
            output_dir=tmp_path,
            template_dir=tmp_path,
            data=self._game_data,
        )

        # Register the save pitcher
        scorecard.new_inning()
        scorecard.new_inning().pitching_substitution(10)

        # Winning team: FOO
        # WP: FOO #1 John Doe
        scorecard.winning_pitcher(1, is_away_team=True)

        # SV: FOO #10 John Doe
        scorecard.save_pitcher(10, is_away_team=True)

        # Loser team: BAR
        # LP: BAR #21 Jack Doe
        scorecard.losing_pitcher(21)

        scorecard.generate_scorecard()

        assert filecmp.cmp(
            os.path.join(expected_results_folder, "scorecard_home.mp"),
            tmp_path / "scorecard_home.mp",
        )

        assert filecmp.cmp(
            os.path.join(expected_results_folder, "scorecard_away.mp"),
            tmp_path / "scorecard_away.mp",
        )

    def test_baseball_scorecard_nine_inning_game_home_win(self, tmp_path):
        """Tests the scenario where a nine inning scorecard is generated.

        This tests the following:
        - Home win with a save pitcher.
        - Pitching errors (balks, wild pitches, passed balls).
        - Fielding errors.
        - General plays (hits, advances, runner thrown out, RBIs, and others).

        The plays are heavily based in the 2024-07-29 SEA @ BOS game, with
        modifications to include certain scenarios that wanted to be tested.
        """

        self._write_empty_templates(tmp_path)

        expected_results_folder = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "expected_results",
            "nine_inning_game_home_win",
        )

        scorecard = Scorecard(
            output_dir=tmp_path,
            template_dir=tmp_path,
            data=self._game_data,
        )

        self._nine_inning_game_calls(scorecard)
        scorecard.generate_scorecard()

        assert filecmp.cmp(
            os.path.join(expected_results_folder, "scorecard_home.mp"),
            tmp_path / "scorecard_home.mp",
        )

        assert filecmp.cmp(
            os.path.join(expected_results_folder, "scorecard_away.mp"),
            tmp_path / "scorecard_away.mp",
        )

    def test_baseball_scorecard_nine_inning_game_home_win_string_method(self, tmp_path):
        """Tests the scenario where a nine inning game is printed as a string.

        This tests the following:
        - Using the string built-in method.

        The plays are heavily based in the 2024-07-29 SEA @ BOS game, with
        modifications to include certain scenarios that wanted to be tested.
        """

        scorecard = Scorecard(
            output_dir=tmp_path,
            template_dir=tmp_path,
            data=self._game_data,
        )

        self._nine_inning_game_calls(scorecard)
        assert str(scorecard) == EXPECTED_STR_RESULT

    def test_baseball_scorecard_exceed_minimum_inn_columns(self, tmp_path):
        """Tests the scenario where a game uses more than the default minimum
        number of inning columns."""

        self._write_empty_templates(tmp_path)

        expected_results_folder = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "expected_results",
            "exceed_minimum_inn_columns",
        )

        scorecard = Scorecard(
            output_dir=tmp_path,
            template_dir=tmp_path,
            data=self._game_data,
        )

        # Create a game that requires 16 inning columns
        t1 = scorecard.new_inning()
        for i in range(10):
            t1.new_ab()

        for j in range(14):
            scorecard.new_inning()
            scorecard.new_inning()

        scorecard.generate_scorecard()

        assert filecmp.cmp(
            os.path.join(expected_results_folder, "scorecard_home.mp"),
            tmp_path / "scorecard_home.mp",
        )

        assert filecmp.cmp(
            os.path.join(expected_results_folder, "scorecard_away.mp"),
            tmp_path / "scorecard_away.mp",
        )
