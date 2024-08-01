class Out:
    def __init__(self, play, out_number):
        self.play = play
        self.out_number = out_number
    
    def __str__(self):
        return f'Out #{self.out_number}: {self.play}'
