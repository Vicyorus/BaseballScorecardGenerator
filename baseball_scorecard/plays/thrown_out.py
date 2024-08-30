from baseball_scorecard.plays.waybase import WayBase

class ThrownOut:
    draw_out_functions = {
        1: "draw_out_one",
        2: "draw_out_two",
        3: "draw_out_three",
    }

    thrown_out_locations = {
        "1-2": "cs_second",
        "1-3": "cs_firstthird",
        "1-4": "to_firsthome",
        "2-3": "cs_third",
        "2-4": "to_secondhome",
        "3-4": "to_home",
    }

    def __init__(self, play, start_base, end_base, out_number):
        self.play = play
        self.start = start_base
        self.end = end_base
        self.out_number = out_number

    def get_metapost_data(self):
        thrown_out_key = f"{self.start}-{self.end}"

        waybase = WayBase(self.play, self.start, self.end)

        result = ""
        result += f"    draw({ThrownOut.thrown_out_locations[thrown_out_key]}) withcolor outclr;\n"
        result += waybase.get_metapost_data()
        result += f"    {ThrownOut.draw_out_functions[self.out_number]}(xstart,ystart,clr);\n"
        return result

    def __str__(self):
        return f'Out #{self.out_number}: Thrown out ({self.start} to {self.end}), {self.play}'