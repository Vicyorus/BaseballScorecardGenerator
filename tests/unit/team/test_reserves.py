import pytest
from baseball_scorecard.team.reserves import Reserves
from baseball_scorecard.team.roster import Roster


class TestReserves:
    """Tests the Reserves class."""

    @pytest.fixture(autouse=True)
    def setup_roster_data(self):
        # Set up the roster
        self._roster: Roster = Roster(
            {
                1: "John Doe",
                2: "Jack Doe",
                3: "James Doe",
                4: "Jasper Doe",
                5: "Jordan Doe",
            },
            [1, 5],
            False,
        )

        # Mark these players as being in the lineup.
        self._roster.get_player(3).in_lineup = True
        self._roster.get_player(5).in_lineup = True

        # Set up the bench and bullpen data.
        self._bench_data: list[list[int | str]] = [[2, "C"], [3, "LF"]]
        self._bullpen_data: list[int] = [4, 5]

    def test_get_bench_metapost_data(self):
        """Test that the get_bench_metapost_data method is correct."""
        reserves = Reserves(self._bullpen_data, self._bench_data, self._roster)

        excepted_metadata = (
            "    % bench info\n"
            "    %% bench #1\n"
            "    set_bench_name_vars(1);\n"
            "    label(btex {\\bigsf 2} etex, bench_no) withcolor clr;\n"
            "    label(btex {\\bigsf Jack Doe} etex, bench_name) withcolor clr;\n"
            "    label(btex {\\bigsf C} etex, bench_extra) withcolor clr;\n\n"
            "    %% bench #2\n"
            "    set_bench_name_vars(2);\n"
            "    label(btex {\\bigsf 3} etex, bench_no) withcolor clr;\n"
            "    label(btex {\\bigsf James Doe} etex, bench_name) withcolor clr;\n"
            "    label(btex {\\bigsf LF} etex, bench_extra) withcolor clr;\n"
            "    strikethrough_bench_name(2, clr);\n\n"
        )
        assert reserves.get_bench_metapost_data() == excepted_metadata

    def test_get_bullpen_metapost_data(self):
        """Test that the get_bullpen_metapost_data method is correct."""
        reserves = Reserves(self._bullpen_data, self._bench_data, self._roster)

        excepted_metadata = (
            "    % bullpen info\n"
            "    %% bullpen #1\n"
            "    set_bullpen_name_vars(1);\n"
            "    label(btex {\\bigsf 4} etex, bullpen_no) withcolor clr;\n"
            "    label(btex {\\bigsf Jasper Doe} etex, bullpen_name) withcolor clr;\n"
            "    label(btex {\\bigsf R} etex, bullpen_extra) withcolor clr;\n\n"
            "    %% bullpen #2\n"
            "    set_bullpen_name_vars(2);\n"
            "    label(btex {\\bigsf 5} etex, bullpen_no) withcolor clr;\n"
            "    label(btex {\\bigsf Jordan Doe} etex, bullpen_name) withcolor clr;\n"
            "    label(btex {\\bigsf L} etex, bullpen_extra) withcolor clr;\n"
            "    strikethrough_bullpen_name(2, clr);\n\n"
        )
        assert reserves.get_bullpen_metapost_data() == excepted_metadata

    def test_string_output(self):
        """Test that the string method is printing the expected format."""
        reserves = Reserves(self._bullpen_data, self._bench_data, self._roster)

        excepted_str = (
            "#2 Jack Doe (C)\n"
            "~~#3 James Doe (LF)~~\n"
            "\n"
            "#4 Jasper Doe (P)\n"
            "~~#5 Jordan Doe (P)~~\n"
        )
        assert str(reserves) == excepted_str
