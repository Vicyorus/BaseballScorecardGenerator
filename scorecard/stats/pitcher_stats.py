class PitcherStats:

    pitcher_stats_template = "    label(btex {{\\bigsf {}}} etex, {}) withcolor clr;\n"


    def __init__(self):
        self.decision = []
        self.outs = 0
        self.batters_faced = 0
        self.hits = 0
        self.runs = 0
        self.earned_runs = 0
        self.walks = 0
        self.intent_walks = 0
        self.strikeouts = 0
        self.hits_by_pitch = 0
        self.balks = 0
        self.wild_pitches = 0
        self.home_runs = 0
        self.pitches = 0
        self.strikes = 0

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
            result += PitcherStats.pitcher_stats_template.format("/".join(self.decision), "pitcher_wls")

        result += PitcherStats.pitcher_stats_template.format(self.batters_faced, "pitcher_bf")
        result += PitcherStats.pitcher_stats_template.format(f"{self.outs // 3}.{self.outs % 3}", "pitcher_ip")
        result += PitcherStats.pitcher_stats_template.format(self.hits, "pitcher_h")
        result += PitcherStats.pitcher_stats_template.format(self.runs, "pitcher_r")
        result += PitcherStats.pitcher_stats_template.format(self.earned_runs, "pitcher_er")
        result += PitcherStats.pitcher_stats_template.format(self.walks, "pitcher_bb")
        result += PitcherStats.pitcher_stats_template.format(self.strikeouts, "pitcher_so")
        result += PitcherStats.pitcher_stats_template.format(self.intent_walks, "pitcher_ibb")
        result += PitcherStats.pitcher_stats_template.format(self.hits_by_pitch, "pitcher_hbp")
        result += PitcherStats.pitcher_stats_template.format(self.balks, "pitcher_blk")
        result += PitcherStats.pitcher_stats_template.format(self.wild_pitches, "pitcher_wp")
        result += PitcherStats.pitcher_stats_template.format(self.home_runs, "pitcher_hr")
        result += PitcherStats.pitcher_stats_template.format(self.pitches, "pitcher_pit")
        result += PitcherStats.pitcher_stats_template.format(self.strikes, "pitcher_str")
        result += "\n"

        return result

    def __str__(self):
        stats = []

        if self.decision:
            stats.append(f'{self.decision}')

        stats.append(f'{self.outs // 3}.{self.outs % 3} IP')

        if self.batters_faced:
            stats.append(f'{self.batters_faced} BF')

        if self.hits:
            stats.append(f'{self.hits} H')

        if self.runs:
            stats.append(f'{self.runs} R')

        if self.earned_runs:
            stats.append(f'{self.earned_runs} ER')

        if self.walks:
            stats.append(f'{self.walks} BB')

        if self.intent_walks:
            stats.append(f'{self.intent_walks} IBB')

        if self.strikeouts:
            stats.append(f'{self.strikeouts} SO')

        if self.hits_by_pitch:
            stats.append(f'{self.hits_by_pitch} HBP')

        if self.balks:
            stats.append(f'{self.balks} BLK')

        if self.wild_pitches:
            stats.append(f'{self.wild_pitches} WP')

        if self.home_runs:
            stats.append(f'{self.home_runs} HR')

        if self.pitches:
            stats.append(f'{self.pitches} P')

        if self.strikes:
            stats.append(f'{self.strikes} S')

        return " ".join(stats)