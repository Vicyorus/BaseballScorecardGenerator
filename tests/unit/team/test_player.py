import pytest
from baseball_scorecard.team.player import Player


class TestPlayer:
    """Tests the Player class."""

    @pytest.fixture(autouse=True)
    def setup_player_data(self):
        self._id = 1
        self._number = 1
        self._name = "John Doe"

    def test_set_lineup_position(self):
        """Test that the set_lineup_position method is correct."""
        player = Player(self._id, self._number, self._name)
        player.set_lineup_position("2", 1)

        assert player.in_lineup == True
        assert player.defensive_position == ["2"]
        assert player.inning_entered == 1

    def test_add_defensive_position(self):
        """Test that the add_defensive_position method is correct."""
        player = Player(self._id, self._number, self._name)
        player.add_defensive_position("2")
        player.add_defensive_position("3")
        assert player.defensive_position == ["2", "3"]

    def test_set_primary_position(self):
        """Test that the set_primary_position method is correct."""
        player = Player(self._id, self._number, self._name)
        player.set_primary_position("C")
        assert player.primary_position == "C"

    def test_set_as_bullpen(self):
        """Test that the set_as_bullpen method is correct."""
        player = Player(self._id, self._number, self._name)
        player.set_as_bullpen()
        assert player.primary_position == "P"
        assert player.is_bullpen == True

    def test_add_pitch(self):
        """Test that the add_pitch method is correct."""
        player = Player(self._id, self._number, self._name)
        player.add_pitch()
        assert player.pitcher_stats.pitches == 1
        assert player.pitcher_stats.strikes == 1

        player.add_pitch(is_strike=False)
        assert player.pitcher_stats.pitches == 2
        assert player.pitcher_stats.strikes == 1

    def test_add_decision(self):
        """Test that the add_decision method is correct."""
        player = Player(self._id, self._number, self._name)
        player.add_decision("BS")
        player.add_decision("L")
        assert player.pitcher_stats.decision == ["BS", "L"]

    def test_get_lineup_metapost_data_normal_player(self):
        """Test that the get_lineup_metapost_data method is correct, for a normal player."""
        player = Player(self._id, self._number, self._name)

        expected_metapost = (
            "    %% lineup 1-1\n"
            "    set_batter_name_vars(1, 1);\n"
            "    label.urt(btex {\\bigsf 1} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 0} etex, (inn_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf } etex, (pos_x,player_y)) withcolor clr;\n\n"
        )
        assert player.get_lineup_metapost_data(1, 1) == expected_metapost

    def test_get_lineup_metapost_data_extra_player(self):
        """Test that the get_lineup_metapost_data method is correct, for an extra player."""
        player = Player(self._id, self._number, self._name)

        expected_metapost = (
            "    %% lineup 10-1\n"
            "    set_batter_name_vars(10, 1);\n"
            "    label(btex {\\sf 1} etex, (-324,player_y+32-6)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe (0)} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf } etex, (pos_x,player_y)) withcolor clr;\n\n"
        )
        assert (
            player.get_lineup_metapost_data(
                10, 1, is_extra=True, original_postion_idx=1
            )
            == expected_metapost
        )

    def test_get_bench_metapost_data(self):
        """Test that the get_bench_metapost_data method is correct"""
        player = Player(self._id, self._number, self._name)
        player.set_primary_position("C")

        expected_metapost = (
            "    %% bench #1\n"
            "    set_bench_name_vars(1);\n"
            "    label(btex {\\bigsf 1} etex, bench_no) withcolor clr;\n"
            "    label(btex {\\bigsf John Doe} etex, bench_name) withcolor clr;\n"
            "    label(btex {\\bigsf C} etex, bench_extra) withcolor clr;\n\n"
        )
        assert player.get_bench_metapost_data(1) == expected_metapost

    def test_get_bench_metapost_data_player_in_lineup(self):
        """Test that the get_bench_metapost_data method is correct, for a player in the lineup."""
        player = Player(self._id, self._number, self._name)
        player.set_primary_position("C")
        player.in_lineup = True

        expected_metapost = (
            "    %% bench #1\n"
            "    set_bench_name_vars(1);\n"
            "    label(btex {\\bigsf 1} etex, bench_no) withcolor clr;\n"
            "    label(btex {\\bigsf John Doe} etex, bench_name) withcolor clr;\n"
            "    label(btex {\\bigsf C} etex, bench_extra) withcolor clr;\n"
            "    strikethrough_bench_name(1, clr);\n\n"
        )
        assert player.get_bench_metapost_data(1) == expected_metapost

    def test_get_bullpen_metapost_data(self):
        """Test that the get_bullpen_metapost_data method is correct"""
        player = Player(self._id, self._number, self._name)
        player.set_as_bullpen()

        expected_metapost = (
            "    %% bullpen #1\n"
            "    set_bullpen_name_vars(1);\n"
            "    label(btex {\\bigsf 1} etex, bullpen_no) withcolor clr;\n"
            "    label(btex {\\bigsf John Doe} etex, bullpen_name) withcolor clr;\n"
            "    label(btex {\\bigsf R} etex, bullpen_extra) withcolor clr;\n\n"
        )
        assert player.get_bullpen_metapost_data(1) == expected_metapost

    def test_get_bullpen_metapost_data_left_handed_pitcher(self):
        """Test that the get_bullpen_metapost_data method is correct, for a left-handed pitcher."""
        player = Player(self._id, self._number, self._name, is_lefty=True)
        player.set_as_bullpen()

        expected_metapost = (
            "    %% bullpen #1\n"
            "    set_bullpen_name_vars(1);\n"
            "    label(btex {\\bigsf 1} etex, bullpen_no) withcolor clr;\n"
            "    label(btex {\\bigsf John Doe} etex, bullpen_name) withcolor clr;\n"
            "    label(btex {\\bigsf L} etex, bullpen_extra) withcolor clr;\n\n"
        )
        assert player.get_bullpen_metapost_data(1) == expected_metapost

    def test_get_bullpen_metapost_data_player_in_lineup(self):
        """Test that the get_bullpen_metapost_data method is correct, for a pitcher in the lineup."""
        player = Player(self._id, self._number, self._name)
        player.set_as_bullpen()
        player.in_lineup = True

        expected_metapost = (
            "    %% bullpen #1\n"
            "    set_bullpen_name_vars(1);\n"
            "    label(btex {\\bigsf 1} etex, bullpen_no) withcolor clr;\n"
            "    label(btex {\\bigsf John Doe} etex, bullpen_name) withcolor clr;\n"
            "    label(btex {\\bigsf R} etex, bullpen_extra) withcolor clr;\n"
            "    strikethrough_bullpen_name(1, clr);\n\n"
        )
        assert player.get_bullpen_metapost_data(1) == expected_metapost

    def test_get_pitcher_metapost_data(self):
        """Test that the get_pitcher_metapost_data method is correct"""
        player = Player(self._id, self._number, self._name)
        player.set_lineup_position("1", 1)

        expected_metapost = (
            "    %% pitcher #1\n"
            "    set_pitcher_name_vars(1);\n"
            "    label.urt(btex {\\bigsf 1} etex, pitcher_no) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe} etex, pitcher_name) withcolor clr;\n"
            "    label.urt(btex {\\bigsf R} etex, pitcher_handedness) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, pitcher_inn) withcolor clr;\n\n"
        )
        assert player.get_pitcher_metapost_data(1) == expected_metapost

    def test_get_pitcher_metapost_data_left_handed_pitcher(self):
        """Test that the get_pitcher_metapost_data method is correct, for a left-handed pitcher."""
        player = Player(self._id, self._number, self._name, is_lefty=True)
        player.set_lineup_position("1", 1)

        expected_metapost = (
            "    %% pitcher #1\n"
            "    set_pitcher_name_vars(1);\n"
            "    label.urt(btex {\\bigsf 1} etex, pitcher_no) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe} etex, pitcher_name) withcolor clr;\n"
            "    label.urt(btex {\\bigsf L} etex, pitcher_handedness) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, pitcher_inn) withcolor clr;\n\n"
        )
        assert player.get_pitcher_metapost_data(1) == expected_metapost

    def test_string_output(self):
        """Test that the string method is printing the expected format."""
        player = Player(self._id, self._number, self._name)
        assert str(player) == "#1 John Doe"

    def test_get_reserves_str(self):
        """Test that the get_reserves_str returns the correct string for a reserve player."""
        player = Player(self._id, self._number, self._name)
        player.set_primary_position("C")

        assert player.get_reserves_str() == "#1 John Doe (C)\n"

    @pytest.mark.parametrize(
        "position_code, expected_str",
        [
            ("1", "P #1 John Doe (1) \n"),
            ("2", "C #1 John Doe (1) \n"),
            ("3", "1B #1 John Doe (1) \n"),
            ("4", "2B #1 John Doe (1) \n"),
            ("5", "3B #1 John Doe (1) \n"),
            ("6", "SS #1 John Doe (1) \n"),
            ("7", "LF #1 John Doe (1) \n"),
            ("8", "CF #1 John Doe (1) \n"),
            ("9", "RF #1 John Doe (1) \n"),
            ("0", "DH #1 John Doe (1) \n"),
            ("10", "DH #1 John Doe (1) \n"),
            ("PH", "PH #1 John Doe (1) \n"),
            ("PR", "PR #1 John Doe (1) \n"),
        ],
    )
    def test_get_lineup_str(self, position_code, expected_str):
        """Test that the get_lineup_str returns the correct string for a player in the lineup."""
        player = Player(self._id, self._number, self._name)
        player.set_lineup_position(position_code, 1)

        assert player.get_lineup_str() == expected_str

    def test_get_pitcher_str(self):
        """Test that the get_lineup_str returns the correct string for a pitcher."""
        player = Player(self._id, self._number, self._name)
        player.get_pitcher_str() == "#1 John Doe (1) \n"
