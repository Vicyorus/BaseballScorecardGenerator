import pytest
from baseball_scorecard.team.pitcher_lineup import PitcherLineup
from baseball_scorecard.team.roster import Roster


class TestPitcherLineup:
    """Tests the PitcherLineup class."""

    @pytest.fixture(autouse=True)
    def setup_roster_data(self):
        # Set up the roster
        self._roster: Roster = Roster(
            {
                1: "John Doe",
                2: "Jack Doe",
            },
            [1],
            False,
        )

        # Set the starting and relief pitcher for comparisons.
        self._starting_pitcher = self._roster.get_player(1)
        self._relief_pitcher = self._roster.get_player(2)

        # Set some pitching stats for the pitchers.
        self._starting_pitcher.pitcher_stats.hits = 1
        self._starting_pitcher.pitcher_stats.pitches = 100
        self._starting_pitcher.pitcher_stats.strikes = 50
        self._relief_pitcher.pitcher_stats.hits = 2
        self._relief_pitcher.pitcher_stats.pitches = 20
        self._relief_pitcher.pitcher_stats.strikes = 10

    def test_add_pitcher(self):
        """Test that the add_pitcher method is correct."""

        pitcher_lineup = PitcherLineup(1, self._roster)
        pitcher_lineup.add_pitcher(self._relief_pitcher, 2)

        assert pitcher_lineup.pitchers == [
            self._starting_pitcher,
            self._relief_pitcher,
        ]

    def test_get_current_pitcher(self):
        """Test that the get_current_pitcher method is correct."""

        pitcher_lineup = PitcherLineup(1, self._roster)
        assert pitcher_lineup.get_current_pitcher() == self._starting_pitcher

        pitcher_lineup.add_pitcher(self._relief_pitcher, 2)
        assert pitcher_lineup.get_current_pitcher() == self._relief_pitcher

    def test_get_pitching_totals(self):
        """Test that the get_pitching_totals method is correct."""
        pitcher_lineup = PitcherLineup(1, self._roster)
        pitcher_lineup.add_pitcher(self._relief_pitcher, 2)

        pitching_totals = pitcher_lineup.get_pitching_totals()

        assert pitching_totals.hits == 3
        assert pitching_totals.pitches == 120
        assert pitching_totals.strikes == 60

    def test_get_pitcher_info_metapost_data(self):
        """Test that the get_pitcher_info_metapost_data method is correct."""
        pitcher_lineup = PitcherLineup(1, self._roster)
        pitcher_lineup.add_pitcher(self._relief_pitcher, 2)

        expected_metapost = (
            "    %% pitcher #1\n"
            "    set_pitcher_name_vars(1);\n"
            "    label.urt(btex {\\bigsf 1} etex, pitcher_no) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe} etex, pitcher_name) withcolor clr;\n"
            "    label.urt(btex {\\bigsf L} etex, pitcher_handedness) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, pitcher_inn) withcolor clr;\n\n"
            "    %% pitcher #2\n"
            "    set_pitcher_name_vars(2);\n"
            "    label.urt(btex {\\bigsf 2} etex, pitcher_no) withcolor clr;\n"
            "    label.urt(btex {\\bigsf Jack Doe} etex, pitcher_name) withcolor clr;\n"
            "    label.urt(btex {\\bigsf R} etex, pitcher_handedness) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 2} etex, pitcher_inn) withcolor clr;\n\n"
        )

        assert pitcher_lineup.get_pitcher_info_metapost_data() == expected_metapost

    def test_get_pitcher_stats_metapost_data(self):
        """Test that the get_pitcher_stats_metapost_data method is correct."""
        pitcher_lineup = PitcherLineup(1, self._roster)
        pitcher_lineup.add_pitcher(self._relief_pitcher, 2)

        expected_metapost = (
            "    set_pitcher_total_vars(1);\n"
            "    label(btex {\\bigsf 0} etex, pitcher_bf) withcolor clr;\n"
            "    label(btex {\\bigsf 0.0} etex, pitcher_ip) withcolor clr;\n"
            "    label(btex {\\bigsf 1} etex, pitcher_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_er) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_so) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_ibb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_hbp) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_blk) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_wp) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_hr) withcolor clr;\n"
            "    label(btex {\\bigsf 100} etex, pitcher_pit) withcolor clr;\n"
            "    label(btex {\\bigsf 50} etex, pitcher_str) withcolor clr;\n"
            "\n"
            "    set_pitcher_total_vars(2);\n"
            "    label(btex {\\bigsf 0} etex, pitcher_bf) withcolor clr;\n"
            "    label(btex {\\bigsf 0.0} etex, pitcher_ip) withcolor clr;\n"
            "    label(btex {\\bigsf 2} etex, pitcher_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_er) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_so) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_ibb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_hbp) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_blk) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_wp) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_hr) withcolor clr;\n"
            "    label(btex {\\bigsf 20} etex, pitcher_pit) withcolor clr;\n"
            "    label(btex {\\bigsf 10} etex, pitcher_str) withcolor clr;\n"
            "\n"
            "    set_pitcher_total_vars(13);\n"
            "    label(btex {\\bigsf 0} etex, pitcher_bf) withcolor clr;\n"
            "    label(btex {\\bigsf 0.0} etex, pitcher_ip) withcolor clr;\n"
            "    label(btex {\\bigsf 3} etex, pitcher_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_er) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_so) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_ibb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_hbp) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_blk) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_wp) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_hr) withcolor clr;\n"
            "    label(btex {\\bigsf 120} etex, pitcher_pit) withcolor clr;\n"
            "    label(btex {\\bigsf 60} etex, pitcher_str) withcolor clr;\n"
            "\n"
        )

        assert pitcher_lineup.get_pitcher_stats_metapost_data() == expected_metapost

    def test_string_output(self):
        """Test that the string method is printing the expected format."""
        pitcher_lineup = PitcherLineup(1, self._roster)
        pitcher_lineup.add_pitcher(self._relief_pitcher, 2)
        expected_str = (
            "#1 John Doe (1) 0.0 IP 1 H 100 P 50 S\n"
            "#2 Jack Doe (2) 0.0 IP 2 H 20 P 10 S\n"
        )
        assert str(pitcher_lineup) == expected_str
