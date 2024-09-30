import pytest
from baseball_scorecard.stats.pitcher_stats import PitcherStats


@pytest.mark.parametrize(
    "data, expected_metapost, expected_str",
    [
        (
            {
                "decision": ["BS", "L"],
                "outs": 27,
                "batters_faced": 32,
                "hits": 1,
                "runs": 1,
                "earned_runs": 1,
                "walks": 1,
                "intent_walks": 1,
                "strikeouts": 1,
                "hits_by_pitch": 1,
                "balks": 1,
                "wild_pitches": 1,
                "home_runs": 1,
                "pitches": 100,
                "strikes": 70,
            },
            (
                "    set_pitcher_total_vars(1);\n"
                "    label(btex {\\bigsf BS/L} etex, pitcher_wls) withcolor clr;\n"
                "    label(btex {\\bigsf 32} etex, pitcher_bf) withcolor clr;\n"
                "    label(btex {\\bigsf 9.0} etex, pitcher_ip) withcolor clr;\n"
                "    label(btex {\\bigsf 1} etex, pitcher_h) withcolor clr;\n"
                "    label(btex {\\bigsf 1} etex, pitcher_r) withcolor clr;\n"
                "    label(btex {\\bigsf 1} etex, pitcher_er) withcolor clr;\n"
                "    label(btex {\\bigsf 1} etex, pitcher_bb) withcolor clr;\n"
                "    label(btex {\\bigsf 1} etex, pitcher_so) withcolor clr;\n"
                "    label(btex {\\bigsf 1} etex, pitcher_ibb) withcolor clr;\n"
                "    label(btex {\\bigsf 1} etex, pitcher_hbp) withcolor clr;\n"
                "    label(btex {\\bigsf 1} etex, pitcher_blk) withcolor clr;\n"
                "    label(btex {\\bigsf 1} etex, pitcher_wp) withcolor clr;\n"
                "    label(btex {\\bigsf 1} etex, pitcher_hr) withcolor clr;\n"
                "    label(btex {\\bigsf 100} etex, pitcher_pit) withcolor clr;\n"
                "    label(btex {\\bigsf 70} etex, pitcher_str) withcolor clr;\n\n"
            ),
            "BS/L 9.0 IP 32 BF 1 H 1 R 1 ER 1 BB 1 IBB 1 SO 1 HBP 1 BLK 1 WP 1 HR 100 P 70 S",
        ),
    ],
)
class TestPitcherStats:
    """Tests the PitcherStats class."""

    def test_get_metapost_data(self, data, expected_metapost, expected_str):
        """Test that the get_metapost_data method is correct."""

        other_pitcher_stats = PitcherStats()
        other_pitcher_stats.outs = data["outs"]
        other_pitcher_stats.batters_faced = data["batters_faced"]
        other_pitcher_stats.hits = data["hits"]
        other_pitcher_stats.runs = data["runs"]
        other_pitcher_stats.earned_runs = data["earned_runs"]
        other_pitcher_stats.walks = data["walks"]
        other_pitcher_stats.intent_walks = data["intent_walks"]
        other_pitcher_stats.strikeouts = data["strikeouts"]
        other_pitcher_stats.hits_by_pitch = data["hits_by_pitch"]
        other_pitcher_stats.balks = data["balks"]
        other_pitcher_stats.wild_pitches = data["wild_pitches"]
        other_pitcher_stats.home_runs = data["home_runs"]
        other_pitcher_stats.pitches = data["pitches"]
        other_pitcher_stats.strikes = data["strikes"]

        pitcher_stats = PitcherStats()
        pitcher_stats.add_stats(other_pitcher_stats)
        for decision in data["decision"]:
            pitcher_stats.add_decision(decision)

        assert pitcher_stats.get_metapost_data(1) == expected_metapost

    def test_string_output(self, data, expected_metapost, expected_str):
        """Test that the string method is printing the expected format."""
        pitcher_stats = PitcherStats()
        for decision in data["decision"]:
            pitcher_stats.add_decision(decision)

        pitcher_stats.outs = data["outs"]
        pitcher_stats.batters_faced = data["batters_faced"]
        pitcher_stats.hits = data["hits"]
        pitcher_stats.runs = data["runs"]
        pitcher_stats.earned_runs = data["earned_runs"]
        pitcher_stats.walks = data["walks"]
        pitcher_stats.intent_walks = data["intent_walks"]
        pitcher_stats.strikeouts = data["strikeouts"]
        pitcher_stats.hits_by_pitch = data["hits_by_pitch"]
        pitcher_stats.balks = data["balks"]
        pitcher_stats.wild_pitches = data["wild_pitches"]
        pitcher_stats.home_runs = data["home_runs"]
        pitcher_stats.pitches = data["pitches"]
        pitcher_stats.strikes = data["strikes"]

        assert str(pitcher_stats) == expected_str
