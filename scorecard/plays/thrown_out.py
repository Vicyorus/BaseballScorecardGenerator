class ThrownOut:

    def __init__(self, play, start_base, end_base, out_number):
        self.play = play
        self.start = start_base
        self.end = end_base
        self.out_number = out_number

    def __str__(self):
        return f'Out #{self.out_number}: Thrown out ({self.start} to {self.end}), {self.play}'