class PitcherStats:

    def __init__(self):
        self.decision: list[str] = []
        self.outs: int = 0
        self.batters_faced: int = 0
        self.hits: int = 0
        self.runs: int = 0
        self.earned_runs: int = 0
        self.walks: int = 0
        self.intent_walks: int = 0
        self.strikeouts: int = 0
        self.hits_by_pitch: int = 0
        self.balks: int = 0
        self.wild_pitches: int = 0
        self.home_runs: int = 0
        self.pitches: int = 0
        self.strikes: int = 0

    def add_decision(self, decision):
        self.decision.append(decision)

    def add_stats(self, other_pitcher_stats):
        self.outs += other_pitcher_stats.outs
        self.batters_faced += other_pitcher_stats.batters_faced
        self.hits += other_pitcher_stats.hits
        self.runs += other_pitcher_stats.runs
        self.earned_runs += other_pitcher_stats.earned_runs
        self.walks += other_pitcher_stats.walks
        self.intent_walks += other_pitcher_stats.intent_walks
        self.strikeouts += other_pitcher_stats.strikeouts
        self.hits_by_pitch += other_pitcher_stats.hits_by_pitch
        self.balks += other_pitcher_stats.balks
        self.wild_pitches += other_pitcher_stats.wild_pitches
        self.home_runs += other_pitcher_stats.home_runs
        self.pitches += other_pitcher_stats.pitches
        self.strikes += other_pitcher_stats.strikes

    def get_metapost_data(self, index):
        result = f"    set_pitcher_total_vars({index});\n"

        if len(self.decision) != 0:
            result += f"    label(btex {{\\bigsf {'/'.join(self.decision)}}} etex, pitcher_wls) withcolor clr;\n"

        result += (
            f"    label(btex {{\\bigsf {self.batters_faced}}} etex, pitcher_bf) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.outs // 3}.{self.outs % 3}}} etex, pitcher_ip) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.hits}}} etex, pitcher_h) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.runs}}} etex, pitcher_r) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.earned_runs}}} etex, pitcher_er) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.walks}}} etex, pitcher_bb) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.strikeouts}}} etex, pitcher_so) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.intent_walks}}} etex, pitcher_ibb) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.hits_by_pitch}}} etex, pitcher_hbp) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.balks}}} etex, pitcher_blk) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.wild_pitches}}} etex, pitcher_wp) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.home_runs}}} etex, pitcher_hr) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.pitches}}} etex, pitcher_pit) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.strikes}}} etex, pitcher_str) withcolor clr;\n\n"
        )

        return result

    def __str__(self):
        stats = []

        if self.decision:
            stats.append(f"{'/'.join(self.decision)}")

        stats.append(f"{self.outs // 3}.{self.outs % 3} IP")

        if self.batters_faced:
            stats.append(f"{self.batters_faced} BF")

        if self.hits:
            stats.append(f"{self.hits} H")

        if self.runs:
            stats.append(f"{self.runs} R")

        if self.earned_runs:
            stats.append(f"{self.earned_runs} ER")

        if self.walks:
            stats.append(f"{self.walks} BB")

        if self.intent_walks:
            stats.append(f"{self.intent_walks} IBB")

        if self.strikeouts:
            stats.append(f"{self.strikeouts} SO")

        if self.hits_by_pitch:
            stats.append(f"{self.hits_by_pitch} HBP")

        if self.balks:
            stats.append(f"{self.balks} BLK")

        if self.wild_pitches:
            stats.append(f"{self.wild_pitches} WP")

        if self.home_runs:
            stats.append(f"{self.home_runs} HR")

        if self.pitches:
            stats.append(f"{self.pitches} P")

        if self.strikes:
            stats.append(f"{self.strikes} S")

        return " ".join(stats)
