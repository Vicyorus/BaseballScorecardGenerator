class Out:
    draw_out_functions = {
        1: "draw_out_one",
        2: "draw_out_two",
        3: "draw_out_three",
    }

    def __init__(self, play, out_number):
        self.play = play
        self.out_number = out_number

    def get_metapost_data(self):
        result = ""
        if self.play == "!K":
            result += "    draw_strikeout_looking(outlabel, outclr);\n"
        else:
            result += f"    label(btex {{\\bigsf {self.play}}} etex, outlabel) withcolor outclr;\n"

        result += f"    {Out.draw_out_functions[self.out_number]}(xstart,ystart,clr);\n"

        return result

    def __str__(self):
        return f'Out #{self.out_number}: {self.play}'
