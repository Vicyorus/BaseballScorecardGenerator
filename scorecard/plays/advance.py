class Advance:
    def __init__(self, play, start_base, end_base):
        self.play = play
        self.start = start_base
        self.end = end_base

    def __str__(self):
        return f'Advance ({self.start} to {self.end}): {self.play}'
