import pytest
from baseball_scorecard.stats.inning_stats import InningStats


@pytest.mark.parametrize(
    "data, expected_metapost, expected_str",
    [
        (
            {
                "runs": 1,
                "hits": 2,
                "errors": 3,
                "left_on_base": 4,
                "walks": 5,
                "strikeouts": 6,
                "pitches": 7,
                "strikes": 8,
            },
            (
                "    % inning stats\n"
                f"    set_inning_total_vars(xstart);\n"
                f"    label(btex {{\\bigsf 1}} etex, inn_run) withcolor clr;\n"
                f"    label(btex {{\\bigsf 2}} etex, inn_hit) withcolor clr;\n"
                f"    label(btex {{\\bigsf 3}} etex, inn_err) withcolor clr;\n"
                f"    label(btex {{\\bigsf 4}} etex, inn_lob) withcolor clr;\n"
                f"    label(btex {{\\bigsf 5}} etex, inn_bb) withcolor clr;\n"
                f"    label(btex {{\\bigsf 6}} etex, inn_so) withcolor clr;\n"
                f"    label(btex {{\\bigsf 7}} etex, inn_pit) withcolor clr;\n"
                f"    label(btex {{\\bigsf 8}} etex, inn_str) withcolor clr;\n\n"
            ),
            "Inning totals: 1 R 2 H 3 E 4 LOB 5 BB 6 K 7 P 8 S\n",
        ),
    ],
)
class TestInningStats:
    """Tests the InningStats class."""

    def test_get_metapost_data(self, data, expected_metapost, expected_str):
        """Test that the get_metapost_data method is correct."""

        inning_stats = InningStats()
        inning_stats.runs = data["runs"]
        inning_stats.hits = data["hits"]
        inning_stats.errors = data["errors"]
        inning_stats.left_on_base = data["left_on_base"]
        inning_stats.strikeouts = data["strikeouts"]
        inning_stats.walks = data["walks"]
        inning_stats.pitches = data["pitches"]
        inning_stats.strikes = data["strikes"]

        assert inning_stats.get_metapost_data() == expected_metapost

    def test_string_output(self, data, expected_metapost, expected_str):
        """Test that the string method is printing the expected format."""
        inning_stats = InningStats()
        inning_stats.runs = data["runs"]
        inning_stats.hits = data["hits"]
        inning_stats.errors = data["errors"]
        inning_stats.left_on_base = data["left_on_base"]
        inning_stats.strikeouts = data["strikeouts"]
        inning_stats.walks = data["walks"]
        inning_stats.pitches = data["pitches"]
        inning_stats.strikes = data["strikes"]

        assert str(inning_stats) == expected_str
