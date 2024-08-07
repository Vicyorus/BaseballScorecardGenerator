class Pitch:
    def __init__(self, pitch_code, inc_pitch_count, is_strike=True):
        self.pitch_code = pitch_code
        self.is_strike = is_strike
        self.inc_pitch_count = inc_pitch_count

    def __str__(self):
        return f'{self.pitch_code}'
