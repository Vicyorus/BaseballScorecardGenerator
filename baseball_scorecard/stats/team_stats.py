from baseball_scorecard.stats.pitcher_stats import PitcherStats


class TeamStats:

    def __init__(self):
        # Stats that will be filled up from the direct calls.
        self.runs: int = 0
        self.hits: dict[int, int] = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
        }
        self.sac_flys: int = 0
        self.sac_bunts: int = 0
        self.passed_balls: int = 0
        self.stolen_bases: int = 0
        self.caught_stealing: int = 0
        self.picked_off: int = 0
        self.double_plays: int = 0
        self.triple_plays: int = 0
        self.errors: int = 0
        self.left_on_base: int = 0
        self.risp_at_bats: int = 0
        self.risp_hits: int = 0

        # At-bats to be calculated from the team's totals.
        self.at_bats: int = 0

        # Stats that are calculated from the opposing pitcher stats.
        self.outs: int = 0
        self.hit_by_pitch: int = 0
        self.walks: int = 0
        self.intent_walks: int = 0
        self.strikeouts: int = 0
        self.balks: int = 0
        self.wild_pitches: int = 0
        self.pitches: int = 0
        self.strikes: int = 0

    def get_metapost_data(
        self, total_at_bats: int, pitching_stats: PitcherStats
    ) -> str:
        # Add the pitching stats to the team stats.
        self.__add_pitching_stats(pitching_stats)

        # Add the at-bats to the team stats.
        self.at_bats = total_at_bats

        # Generate the totals for the game.
        result = self.__get_game_total_metapost_data()

        result += "\n"

        # Generate the basepath totals for the game.
        result += self.__get_basepath_metapost_data()
        return result

    def __add_pitching_stats(self, pitching_stats: PitcherStats):
        self.outs = pitching_stats.outs
        self.hit_by_pitch = pitching_stats.hits_by_pitch
        self.walks = pitching_stats.walks
        self.intent_walks = pitching_stats.intent_walks
        self.strikeouts = pitching_stats.strikeouts
        self.balks = pitching_stats.balks
        self.wild_pitches = pitching_stats.wild_pitches
        self.pitches = pitching_stats.pitches
        self.strikes = pitching_stats.strikes

    def __get_game_total_metapost_data(self) -> str:
        # Calculate the hits.
        hits = 0
        for _, hit_count in self.hits.items():
            hits += hit_count

        result = "    %% game totals\n"
        result += (
            "    set_game_total_vars(innings);\n"
            f"    label(btex {{\\bigsf {self.runs}}} etex, inn_run) withcolor clr;\n"
            f"    label(btex {{\\bigsf {hits}}} etex, inn_hit) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.errors}}} etex, inn_err) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.left_on_base}}} etex, inn_lob) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.walks + self.intent_walks}}} etex, inn_bb) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.strikeouts}}} etex, inn_so) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.pitches}}} etex, inn_pit) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.strikes}}} etex, inn_str) withcolor clr;\n"
        )
        return result

    def __get_basepath_metapost_data(self) -> str:

        # Calculate the total bases.
        total_bases = 0
        for i in range(1, 5):
            total_bases += self.hits[i] * i

        # Generate the final result.
        result = (
            "    %% basepaths totals\n"
            "    set_basepath_total_vars(innings);\n"
            f"    label.urt(btex {{\\sf {self.hits[1]}}} etex, basepath_first_label) withcolor clr;\n"
            f"    label.urt(btex {{\\sf {self.hits[2]}}} etex, basepath_second_label) withcolor clr;\n"
            f"    label.urt(btex {{\\sf {self.hits[3]}}} etex, basepath_third_label) withcolor clr;\n"
            f"    label.urt(btex {{\\sf {self.hits[4]}}} etex, basepath_hr_label) withcolor clr;\n"
            f"    label.urt(btex {{\\sf {self.sac_flys}}} etex, basepath_sf_label) withcolor clr;\n"
            f"    label.urt(btex {{\\sf {self.sac_bunts}}} etex, basepath_sac_label) withcolor clr;\n"
            "\n"
            f"    label.urt(btex {{\\sf {total_bases}}} etex, basepath_tb_label) withcolor clr;\n"
            f"    label.urt(btex {{\\sf {self.hit_by_pitch}}} etex, basepath_hbp_label) withcolor clr;\n"
            f"    label.urt(btex {{\\sf {self.intent_walks}}} etex, basepath_ibb_label) withcolor clr;\n"
            f"    label.urt(btex {{\\sf {self.balks}}} etex, basepath_blk_label) withcolor clr;\n"
            f"    label.urt(btex {{\\sf {self.wild_pitches}}} etex, basepath_wp_label) withcolor clr;\n"
            f"    label.urt(btex {{\\sf {self.passed_balls}}} etex, basepath_pb_label) withcolor clr;\n"
            "\n"
            f"    label.urt(btex {{\\sf {self.stolen_bases}}} etex, basepath_sb_label) withcolor clr;\n"
            f"    label.urt(btex {{\\sf {self.caught_stealing}}} etex, basepath_cs_label) withcolor clr;\n"
            f"    label.urt(btex {{\\sf {self.picked_off}}} etex, basepath_po_label) withcolor clr;\n"
            f"    label.urt(btex {{\\sf {self.double_plays}}} etex, basepath_dp_label) withcolor clr;\n"
            f"    label.urt(btex {{\\sf {self.triple_plays}}} etex, basepath_tp_label) withcolor clr;\n"
            f"    label(btex {{\\sf {self.risp_hits}-{self.risp_at_bats}}} etex, basepath_risp_label) withcolor clr;\n"
            "\n"
        )

        # Generate the proof strings.
        basepath_totals = "{}+{}+{}+{}+{}~~=~~{}".format(
            self.at_bats,
            self.walks + self.intent_walks,
            self.hit_by_pitch,
            self.sac_bunts,
            self.sac_flys,
            self.at_bats
            + self.walks
            + self.intent_walks
            + self.hit_by_pitch
            + self.sac_bunts
            + self.sac_flys,
        )
        basepath_run_lob_opo = "{}+{}+{}~~=~~{}".format(
            self.runs,
            self.left_on_base,
            self.outs,
            self.runs + self.left_on_base + self.outs,
        )
        result += (
            f"    label.urt(btex {{\\sf {basepath_totals}}} etex, basepath_totals_label) withcolor clr;\n"
            f"    label.urt(btex {{\\sf {basepath_run_lob_opo}}} etex, basepath_run_lob_opo_label) withcolor clr;\n"
        )

        return result

    def __str__(self):
        result = (
            f"R: {self.runs}\n"
            f"1B: {self.hits[1]}\n"
            f"2B: {self.hits[2]}\n"
            f"3B: {self.hits[3]}\n"
            f"HR: {self.hits[4]}\n"
            f"SAC: {self.sac_bunts}\n"
            f"SF: {self.sac_flys}\n"
            f"DP: {self.double_plays}\n"
            f"TP: {self.triple_plays}\n"
            f"SB: {self.stolen_bases}\n"
            f"CS: {self.caught_stealing}\n"
            f"PO: {self.picked_off}\n"
            f"PB: {self.passed_balls}\n"
            f"E: {self.errors}\n"
            f"LOB: {self.left_on_base}\n"
            f"RISP: {self.risp_hits}-{self.risp_at_bats}\n"
        )

        return result
