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
        "Hit1": {"color": "hit", "in_play_box": True, "play_code": "1B"},
        "Hit2": {"color": "hit", "in_play_box": True, "play_code": "2B"},
        "Hit3": {"color": "hit", "in_play_box": True, "play_code": "3B"},
        "Hit4": {"color": "homer", "in_play_box": True, "play_code": "HR"},
        "HitU": {"color": "homer", "in_play_box": True, "play_code": "HR"},
        "Intent Walk": {"color": "walk", "in_play_box": True, "play_code": "IBB"},
        "Walk": {"color": "walk", "in_play_box": True, "play_code": "BB"},
        "Hit By Pitch": {"color": "clr", "in_play_box": True, "play_code": "HBP"},
        "Error": {"color": "error", "in_play_box": False},
        "Reach": {"color": "clr", "in_play_box": False},
        "Advance": {"color": "clr", "in_play_box": False},
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
        if advance_info['in_play_box']:
            result += f"    label(btex {{\\midsf {advance_info['play_code']}}} etex, playloc) withcolor {advance_info['color']};\n"
        else:
            result += WayBase(self.play, self.start, self.end).get_metapost_data()

        result += f"    draw({Advance.advance_locations[advance_location_key]['path']}) withcolor {advance_info['color']};\n"
        return result

    def __str__(self):
        return f'Advance ({self.start} to {self.end}): {self.advance_code} on {self.play}'
