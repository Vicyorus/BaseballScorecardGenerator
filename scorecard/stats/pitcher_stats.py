class PitcherStats:
    def __init__(self):
        self.decision = ""
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