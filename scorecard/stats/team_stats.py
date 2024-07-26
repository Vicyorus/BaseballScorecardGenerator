class TeamStats:
    def __init__(self):
        self.runs = 0
        self.singles = 0
        self.doubles = 0
        self.triples = 0
        self.home_runs = 0
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

    def __str__(self):
        return f'DPs: {self.double_plays}'