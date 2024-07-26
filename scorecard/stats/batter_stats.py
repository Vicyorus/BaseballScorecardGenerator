class BatterStats:
    def __init__(self):
        self.at_bats = 0
        self.runs = 0
        self.hits = 0
        self.rbis = 0
        self.walks = 0
        self.strikeouts = 0

    def __str__(self):
        stats = []

        if self.at_bats:
            stats.append(f'{self.at_bats} AB')

        if self.runs:
            stats.append(f'{self.runs} R')

        if self.hits:
            stats.append(f'{self.hits} H')

        if self.rbis:
            stats.append(f'{self.rbis} RBI')

        if self.walks:
            stats.append(f'{self.walks} BB')

        if self.strikeouts:
            stats.append(f'{self.strikeouts} SO')

        return " ".join(stats)