from scorecard.plays.waybase import WayBase

class Advance:

    advance_locations = {
        "0-1": {"path": "single"},
        "0-2": {"path": "double"},
        "0-3": {"path": "triple"},
        "0-4": {"path": "homerun"},
        "0-U": {"path": "homerun"},
        "1-2": {"path": "firstsecond"},
        "1-3": {"path": "firstthird"},
        "1-4": {"path": "firsthome"},
        "1-U": {"path": "firsthome"},
        "2-3": {"path": "secondthird"},
        "2-4": {"path": "secondhome"},
        "2-U": {"path": "secondhome"},
        "3-4": {"path": "thirdhome"},
        "3-U": {"path": "thirdhome"},
    }

#hr, threeb, twob, oneb, bb, hp

    advance_info = {
        "Hit1": {"color": "hit", "use_circle": True, "circle_code": "oneb"},
        "Hit2": {"color": "hit", "use_circle": True, "circle_code": "twob"},
        "Hit3": {"color": "hit", "use_circle": True, "circle_code": "threeb"},
        "Hit4": {"color": "homer", "use_circle": True, "circle_code": "hr"},
        "HitU": {"color": "homer", "use_circle": True, "circle_code": "hr"},
        "Intent Walk": {"color": "walk", "use_circle": True, "circle_code": "ibb"},
        "Walk": {"color": "walk", "use_circle": True, "circle_code": "bb"},
        "Hit By Pitch": {"color": "clr", "use_circle": True, "circle_code": "hp"},
        "Error": {"color": "error", "use_circle": False},
        "Reach": {"color": "clr", "use_circle": False},
        "Advance": {"color": "clr", "use_circle": False},
    }

    def __init__(self, advance_code, play, start_base, end_base):
        self.advance_code = advance_code
        self.play = play
        self.start = start_base
        self.end = end_base

    def get_metapost_data(self):
        advance_location_key = f"{self.start}-{self.end}"
        advance_info_key = self.advance_code

        if self.advance_code == "Hit":
            advance_info_key = f"{self.advance_code}{self.play}"

        advance_info = Advance.advance_info[advance_info_key]

        result = ""
        if advance_info['use_circle']:
            if advance_info['circle_code'] == "ibb":
                result += "    draw_ibb(bb, clr, walk);\n"
            else:
                result += f"    draw_circle({advance_info['circle_code']}, {advance_info['color']});\n"
        else:
            result += WayBase(self.play, self.start, self.end).get_metapost_data()

        result += f"    draw({Advance.advance_locations[advance_location_key]['path']}) withcolor {advance_info['color']};\n"
        return result

    def __str__(self):
        return f'Advance ({self.start} to {self.end}): {self.advance_code} on {self.play}'
