import pytest
from baseball_scorecard.stats.team_stats import TeamStats
from baseball_scorecard.stats.pitcher_stats import PitcherStats


@pytest.mark.parametrize(
    "data, expected_metapost, expected_str",
    [
        (
            {
                "runs": 1,
                "hits": {
                    1: 1,
                    2: 1,
                    3: 1,
                    4: 1,
                },
                "sac_flys": 1,
                "sac_bunts": 1,
                "passed_balls": 1,
                "stolen_bases": 1,
                "caught_stealing": 1,
                "picked_off": 1,
                "double_plays": 1,
                "triple_plays": 1,
                "errors": 1,
                "left_on_base": 1,
                "at_bats": 1,
                "outs": 1,
                "hits_by_pitch": 1,
                "walks": 1,
                "intent_walks": 1,
                "strikeouts": 1,
                "balks": 1,
                "wild_pitches": 1,
                "pitches": 1,
                "strikes": 1,
                "risp_abs": 2,
                "risp_hits": 1,
            },
            (
                "    %% game totals\n"
                "    set_game_total_vars(innings);\n"
                "    label(btex {\\bigsf 1} etex, inn_run) withcolor clr;\n"
                "    label(btex {\\bigsf 4} etex, inn_hit) withcolor clr;\n"
                "    label(btex {\\bigsf 1} etex, inn_err) withcolor clr;\n"
                "    label(btex {\\bigsf 1} etex, inn_lob) withcolor clr;\n"
                "    label(btex {\\bigsf 2} etex, inn_bb) withcolor clr;\n"
                "    label(btex {\\bigsf 1} etex, inn_so) withcolor clr;\n"
                "    label(btex {\\bigsf 1} etex, inn_pit) withcolor clr;\n"
                "    label(btex {\\bigsf 1} etex, inn_str) withcolor clr;\n"
                "\n"
                "    %% basepaths totals\n"
                "    set_basepath_total_vars(innings);\n"
                "    label.urt(btex {\\sf 1} etex, basepath_first_label) withcolor clr;\n"
                "    label.urt(btex {\\sf 1} etex, basepath_second_label) withcolor clr;\n"
                "    label.urt(btex {\\sf 1} etex, basepath_third_label) withcolor clr;\n"
                "    label.urt(btex {\\sf 1} etex, basepath_hr_label) withcolor clr;\n"
                "    label.urt(btex {\\sf 1} etex, basepath_sf_label) withcolor clr;\n"
                "    label.urt(btex {\\sf 1} etex, basepath_sac_label) withcolor clr;\n"
                "\n"
                "    label.urt(btex {\\sf 10} etex, basepath_tb_label) withcolor clr;\n"
                "    label.urt(btex {\\sf 1} etex, basepath_hbp_label) withcolor clr;\n"
                "    label.urt(btex {\\sf 1} etex, basepath_ibb_label) withcolor clr;\n"
                "    label.urt(btex {\\sf 1} etex, basepath_blk_label) withcolor clr;\n"
                "    label.urt(btex {\\sf 1} etex, basepath_wp_label) withcolor clr;\n"
                "    label.urt(btex {\\sf 1} etex, basepath_pb_label) withcolor clr;\n"
                "\n"
                "    label.urt(btex {\\sf 1} etex, basepath_sb_label) withcolor clr;\n"
                "    label.urt(btex {\\sf 1} etex, basepath_cs_label) withcolor clr;\n"
                "    label.urt(btex {\\sf 1} etex, basepath_po_label) withcolor clr;\n"
                "    label.urt(btex {\\sf 1} etex, basepath_dp_label) withcolor clr;\n"
                "    label.urt(btex {\\sf 1} etex, basepath_tp_label) withcolor clr;\n"
                "    label(btex {\\sf 1-2} etex, basepath_risp_label) withcolor clr;\n"
                "\n"
                "    label.urt(btex {\\sf 33+2+1+1+1~~=~~38} etex, basepath_totals_label) withcolor clr;\n"
                "    label.urt(btex {\\sf 1+1+1~~=~~3} etex, basepath_run_lob_opo_label) withcolor clr;\n"
            ),
            (
                "R: 1\n"
                "1B: 1\n"
                "2B: 1\n"
                "3B: 1\n"
                "HR: 1\n"
                "SAC: 1\n"
                "SF: 1\n"
                "DP: 1\n"
                "TP: 1\n"
                "SB: 1\n"
                "CS: 1\n"
                "PO: 1\n"
                "PB: 1\n"
                "E: 1\n"
                "LOB: 1\n"
                "RISP: 1-2\n"
            ),
        ),
    ],
)
class TestTeamStats:
    """Tests the TeamStats class."""

    def test_get_metapost_data(self, data, expected_metapost, expected_str):
        """Test that the get_metapost_data method is correct."""

        team_stats = TeamStats()
        team_stats.runs = data["runs"]
        team_stats.hits[1] = data["hits"][1]
        team_stats.hits[2] = data["hits"][2]
        team_stats.hits[3] = data["hits"][3]
        team_stats.hits[4] = data["hits"][4]
        team_stats.sac_flys = data["sac_flys"]
        team_stats.sac_bunts = data["sac_bunts"]
        team_stats.passed_balls = data["passed_balls"]
        team_stats.stolen_bases = data["stolen_bases"]
        team_stats.caught_stealing = data["caught_stealing"]
        team_stats.picked_off = data["picked_off"]
        team_stats.double_plays = data["double_plays"]
        team_stats.triple_plays = data["triple_plays"]
        team_stats.errors = data["errors"]
        team_stats.left_on_base = data["left_on_base"]
        team_stats.risp_at_bats = data["risp_abs"]
        team_stats.risp_hits = data["risp_hits"]

        team_stats.at_bats = data["at_bats"]

        pitching_stats = PitcherStats()
        pitching_stats.outs = data["outs"]
        pitching_stats.hits_by_pitch = data["hits_by_pitch"]
        pitching_stats.walks = data["walks"]
        pitching_stats.intent_walks = data["intent_walks"]
        pitching_stats.strikeouts = data["strikeouts"]
        pitching_stats.balks = data["balks"]
        pitching_stats.wild_pitches = data["wild_pitches"]
        pitching_stats.pitches = data["pitches"]
        pitching_stats.strikes = data["strikes"]

        assert team_stats.get_metapost_data(33, pitching_stats) == expected_metapost

    def test_string_output(self, data, expected_metapost, expected_str):
        """Test that the string method is printing the expected format."""
        team_stats = TeamStats()
        team_stats.runs = data["runs"]
        team_stats.hits[1] = data["hits"][1]
        team_stats.hits[2] = data["hits"][2]
        team_stats.hits[3] = data["hits"][3]
        team_stats.hits[4] = data["hits"][4]
        team_stats.sac_flys = data["sac_flys"]
        team_stats.sac_bunts = data["sac_bunts"]
        team_stats.passed_balls = data["passed_balls"]
        team_stats.stolen_bases = data["stolen_bases"]
        team_stats.caught_stealing = data["caught_stealing"]
        team_stats.picked_off = data["picked_off"]
        team_stats.double_plays = data["double_plays"]
        team_stats.triple_plays = data["triple_plays"]
        team_stats.errors = data["errors"]
        team_stats.left_on_base = data["left_on_base"]
        team_stats.risp_at_bats = data["risp_abs"]
        team_stats.risp_hits = data["risp_hits"]

        assert str(team_stats) == expected_str
