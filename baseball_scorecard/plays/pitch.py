class Pitch:
    def __init__(
        self, pitch_code: str, inc_pitch_count: bool = True, is_strike: bool = True
    ):
        self.pitch_code = pitch_code
        self.is_strike = is_strike
        self.inc_pitch_count = inc_pitch_count

    def __str__(self):
        return f"{self.pitch_code}"
