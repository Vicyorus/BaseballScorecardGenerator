class NoAtBat:
    def __init__(self, play):
        self.play = play

    def get_metapost_data(self):
        return f"    label(btex {{\\bigsf {self.play}}} etex, outlabel) withcolor clr;\n"

    def __str__(self):
        return f'No AB: {self.play}'
