from __future__ import annotations


class BatterStats:

    def __init__(self):
        self.at_bats: int = 0
        self.runs: int = 0
        self.hits: int = 0
        self.rbis: int = 0
        self.walks: int = 0
        self.strikeouts: int = 0

    def add_stats(self, other_batter_stats: BatterStats):
        self.at_bats += other_batter_stats.at_bats
        self.runs += other_batter_stats.runs
        self.hits += other_batter_stats.hits
        self.rbis += other_batter_stats.rbis
        self.walks += other_batter_stats.walks
        self.strikeouts += other_batter_stats.strikeouts

    def get_metapost_data(self, position: int, spot: int):
        result = (
            f"    %% batter {position}-{spot}\n"
            f"    set_batter_total_vars({position}, {spot}, innings);\n"
            f"    label(btex {{\\bigsf {self.at_bats}}} etex, batter_ab) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.runs}}} etex, batter_r) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.hits}}} etex, batter_h) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.rbis}}} etex, batter_rbi) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.walks}}} etex, batter_bb) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.strikeouts}}} etex, batter_so) withcolor clr;\n"
        )

        return result

    def __str__(self):
        stats = []

        if self.at_bats:
            stats.append(f"{self.at_bats} AB")

        if self.runs:
            stats.append(f"{self.runs} R")

        if self.hits:
            stats.append(f"{self.hits} H")

        if self.rbis:
            stats.append(f"{self.rbis} RBI")

        if self.walks:
            stats.append(f"{self.walks} BB")

        if self.strikeouts:
            stats.append(f"{self.strikeouts} SO")

        return " ".join(stats)
