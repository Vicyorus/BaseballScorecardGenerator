import pytest
from baseball_scorecard.stats.batter_stats import BatterStats


@pytest.mark.parametrize(
    "data, lineup_pos, pos_spot, expected_metapost, expected_str",
    [
        (
            {
                "at_bats": 1,
                "runs": 2,
                "hits": 3,
                "rbis": 4,
                "walks": 5,
                "strikeouts": 6,
            },
            1,
            1,
            (
                "    %% batter 1-1\n"
                "    set_batter_total_vars(1, 1, innings);\n"
                "    label(btex {\\bigsf 1} etex, batter_ab) withcolor clr;\n"
                "    label(btex {\\bigsf 2} etex, batter_r) withcolor clr;\n"
                "    label(btex {\\bigsf 3} etex, batter_h) withcolor clr;\n"
                "    label(btex {\\bigsf 4} etex, batter_rbi) withcolor clr;\n"
                "    label(btex {\\bigsf 5} etex, batter_bb) withcolor clr;\n"
                "    label(btex {\\bigsf 6} etex, batter_so) withcolor clr;\n"
            ),
            "1 AB 2 R 3 H 4 RBI 5 BB 6 SO",
        ),
    ],
)
class TestBatterStats:
    """Tests the BatterStats class."""

    def test_get_metapost_data(
        self, data, lineup_pos, pos_spot, expected_metapost, expected_str
    ):
        """Test that the get_metapost_data method is correct."""

        other_batter_stats = BatterStats()
        other_batter_stats.at_bats = data["at_bats"]
        other_batter_stats.runs = data["runs"]
        other_batter_stats.hits = data["hits"]
        other_batter_stats.rbis = data["rbis"]
        other_batter_stats.walks = data["walks"]
        other_batter_stats.strikeouts = data["strikeouts"]

        batter_stats = BatterStats()
        batter_stats.add_stats(other_batter_stats)

        assert batter_stats.get_metapost_data(lineup_pos, pos_spot) == expected_metapost

    def test_string_output(
        self, data, lineup_pos, pos_spot, expected_metapost, expected_str
    ):
        """Test that the string method is printing the expected format."""
        batter_stats = BatterStats()
        batter_stats.at_bats = data["at_bats"]
        batter_stats.runs = data["runs"]
        batter_stats.hits = data["hits"]
        batter_stats.rbis = data["rbis"]
        batter_stats.walks = data["walks"]
        batter_stats.strikeouts = data["strikeouts"]
        assert str(batter_stats) == expected_str
