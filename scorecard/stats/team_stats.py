class TeamStats:
    def __init__(self):
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

    def __str__(self):
        result = ""
        result += f'R: {self.runs}\n'
        result += f'1B: {self.hits[1]}\n'
        result += f'2B: {self.hits[2]}\n'
        result += f'3B: {self.hits[3]}\n'
        result += f'HR: {self.hits[4]}\n'
        result += f'SAC: {self.sac_bunts}\n'
        result += f'SF: {self.sac_flys}\n'
        result += f'DP: {self.double_plays}\n'
        result += f'TP: {self.triple_plays}\n'
        result += f'SB: {self.stolen_bases}\n'
        result += f'CS: {self.caught_stealing}\n'
        result += f'PO: {self.picked_off}\n'
        result += f'PB: {self.passed_balls}\n'
        result += f'E: {self.errors}\n'
        result += f'LOB: {self.left_on_base}\n'

        return result
