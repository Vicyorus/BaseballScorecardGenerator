class BatterStats:

    batter_stats_template = "    label(btex {{\\bigsf {}}} etex, {}) withcolor clr;\n"

    def __init__(self):
        self.at_bats = 0
        self.runs = 0
        self.hits = 0
        self.rbis = 0
        self.walks = 0
        self.strikeouts = 0

    def add_stats(self, other_batter_stats):
        self.at_bats += other_batter_stats.at_bats
        self.runs += other_batter_stats.runs
        self.hits += other_batter_stats.hits
        self.rbis += other_batter_stats.rbis
        self.walks += other_batter_stats.walks
        self.strikeouts += other_batter_stats.strikeouts

    def get_metapost_data(self, position, spot):
        result = f"    %% batter {position}-{spot}\n"
        result += f"    set_batter_total_vars({position}, {spot}, innings);\n"
        result += BatterStats.batter_stats_template.format(self.at_bats, "batter_ab")
        result += BatterStats.batter_stats_template.format(self.runs, "batter_r")
        result += BatterStats.batter_stats_template.format(self.hits, "batter_h")
        result += BatterStats.batter_stats_template.format(self.rbis, "batter_rbi")
        result += BatterStats.batter_stats_template.format(self.walks, "batter_bb")
        result += BatterStats.batter_stats_template.format(self.strikeouts, "batter_so")

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
