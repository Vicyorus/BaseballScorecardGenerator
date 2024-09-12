class TeamStats:

    basepath_template = "    label.urt(btex {{\sf {}}} etex, {}) withcolor clr;\n"
    game_totals_template = "    label(btex {{\\bigsf {}}} etex, {}) withcolor clr;\n"

    def __init__(self):
        # Stats that will be filled up from the direct calls.
        self.runs = 0
        self.hits = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
        }
        self.sac_flys = 0
        self.sac_bunts = 0
        self.passed_balls = 0
        self.stolen_bases = 0
        self.caught_stealing = 0
        self.picked_off = 0
        self.double_plays = 0
        self.triple_plays = 0
        self.errors = 0
        self.left_on_base = 0

        # At-bats to be calculated from the team's totals.
        self.at_bats = 0

        # Stats that are calculated from the opposing pitcher stats.
        self.outs = 0
        self.hit_by_pitch = 0
        self.walks = 0
        self.intent_walks = 0
        self.strikeouts = 0
        self.balks = 0
        self.wild_pitches = 0
        self.pitches = 0
        self.strikes = 0

    def get_metapost_data(self, total_at_bats, pitching_stats):
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

    def __add_pitching_stats(self, pitching_stats):
        self.outs = pitching_stats.outs
        self.hit_by_pitch = pitching_stats.hits_by_pitch
        self.walks = pitching_stats.walks
        self.intent_walks = pitching_stats.intent_walks
        self.strikeouts = pitching_stats.strikeouts
        self.balks = pitching_stats.balks
        self.wild_pitches = pitching_stats.wild_pitches
        self.pitches = pitching_stats.pitches
        self.strikes = pitching_stats.strikes

    def __get_game_total_metapost_data(self):
        # Calculate the hits.
        hits = 0
        for _, v in self.hits.items():
            hits += v

        result = "    %% game totals\n"
        result += "    set_game_total_vars(innings);\n"
        result += TeamStats.game_totals_template.format(self.runs, "inn_run")
        result += TeamStats.game_totals_template.format(hits, "inn_hit")
        result += TeamStats.game_totals_template.format(self.errors, "inn_err")
        result += TeamStats.game_totals_template.format(self.left_on_base, "inn_lob")
        result += TeamStats.game_totals_template.format(
            self.walks + self.intent_walks, "inn_bb"
        )
        result += TeamStats.game_totals_template.format(self.strikeouts, "inn_so")
        result += TeamStats.game_totals_template.format(self.pitches, "inn_pit")
        result += TeamStats.game_totals_template.format(self.strikes, "inn_str")

        return result

    def __get_basepath_metapost_data(self):
        # Calculate the total bases.
        total_bases = 0
        for i in range(1, 5):
            total_bases += self.hits[i] * i

        # Generate the final result.
        result = "    %% basepaths totals\n"
        result += "    set_basepath_total_vars(innings);\n"
        result += TeamStats.basepath_template.format(
            self.hits[1], "basepath_first_label"
        )
        result += TeamStats.basepath_template.format(
            self.hits[2], "basepath_second_label"
        )
        result += TeamStats.basepath_template.format(
            self.hits[3], "basepath_third_label"
        )
        result += TeamStats.basepath_template.format(self.hits[4], "basepath_hr_label")
        result += TeamStats.basepath_template.format(self.sac_flys, "basepath_sf_label")
        result += TeamStats.basepath_template.format(
            self.sac_bunts, "basepath_sac_label"
        )
        result += "\n"
        result += TeamStats.basepath_template.format(total_bases, "basepath_tb_label")
        result += TeamStats.basepath_template.format(
            self.hit_by_pitch, "basepath_hbp_label"
        )
        result += TeamStats.basepath_template.format(
            self.intent_walks, "basepath_ibb_label"
        )
        result += TeamStats.basepath_template.format(self.balks, "basepath_blk_label")
        result += TeamStats.basepath_template.format(
            self.wild_pitches, "basepath_wp_label"
        )
        result += TeamStats.basepath_template.format(
            self.passed_balls, "basepath_pb_label"
        )
        result += "\n"
        result += TeamStats.basepath_template.format(
            self.stolen_bases, "basepath_sb_label"
        )
        result += TeamStats.basepath_template.format(
            self.caught_stealing, "basepath_cs_label"
        )
        result += TeamStats.basepath_template.format(
            self.picked_off, "basepath_po_label"
        )
        result += TeamStats.basepath_template.format(
            self.double_plays, "basepath_dp_label"
        )
        result += TeamStats.basepath_template.format(
            self.triple_plays, "basepath_tp_label"
        )
        result += TeamStats.basepath_template.format(self.errors, "basepath_e_label")
        result += "\n"

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
        result += TeamStats.basepath_template.format(
            basepath_totals, "basepath_totals_label"
        )
        result += TeamStats.basepath_template.format(
            basepath_run_lob_opo, "basepath_run_lob_opo_label"
        )

        return result

    def __str__(self):
        result = ""
        result += f"R: {self.runs}\n"
        result += f"1B: {self.hits[1]}\n"
        result += f"2B: {self.hits[2]}\n"
        result += f"3B: {self.hits[3]}\n"
        result += f"HR: {self.hits[4]}\n"
        result += f"SAC: {self.sac_bunts}\n"
        result += f"SF: {self.sac_flys}\n"
        result += f"DP: {self.double_plays}\n"
        result += f"TP: {self.triple_plays}\n"
        result += f"SB: {self.stolen_bases}\n"
        result += f"CS: {self.caught_stealing}\n"
        result += f"PO: {self.picked_off}\n"
        result += f"PB: {self.passed_balls}\n"
        result += f"E: {self.errors}\n"
        result += f"LOB: {self.left_on_base}\n"

        return result
