class WayBase:

    waybase_locations = {
        "0-1": {"location": "wayfirst", "reversed": True, "label_offset": ".lrt"},
        "0-2": {"location": "waysecond", "reversed": True, "label_offset": ".urt"},
        "0-3": {"location": "waythird", "reversed": True, "label_offset": ".ulft"},
        "0-4": {"location": "wayhome", "reversed": True, "label_offset": ".llft"},
        "0-U": {"location": "wayhome", "reversed": True, "label_offset": ".llft"},
        "1-2": {"location": "waysecond", "reversed": True, "number_offset": ".urt", "label_offset": ".urt"},
        "1-3": {"location": "waythird", "reversed": True, "number_offset": ".ulft", "label_offset": ".ulft"},
        "1-4": {"location": "wayhome", "reversed": True, "number_offset": ".lft", "label_offset": ".llft"},
        "1-U": {"location": "wayhome", "reversed": True, "number_offset": ".lft", "label_offset": ".llft"},
        "2-3": {"location": "waythird", "reversed": True, "number_offset": ".ulft", "label_offset": ".ulft"},
        "2-4": {"location": "wayhome", "reversed": True, "number_offset": ".lft", "label_offset": ".llft"},
        "2-U": {"location": "wayhome", "reversed": True, "number_offset": ".lft", "label_offset": ".llft"},
        "3-4": {"location": "wayhome", "reversed": True, "number_offset": ".lft", "label_offset": ".llft"},
        "3-U": {"location": "wayhome", "reversed": True, "number_offset": ".lft", "label_offset": ".llft"},
    }

    waybase_template = "    label{}(btex {{\\sf {}}} etex, {}) withcolor clr;\n"

    def __init__(self, label, start_base, end_base):
        split_label = label.split(" ")
        if len(split_label) == 2:
            self.number = label.split()[0]
            self.label = label.split()[1]
        else:
            self.label = label

        self.start = start_base
        self.end = end_base

    def get_metapost_data(self):
        result = ""
        waybase_key = f"{self.start}-{self.end}"
        waybase_info = WayBase.waybase_locations[waybase_key]

        # If the start is 0 (batter), use only the label.
        if self.start == 0:
            result += WayBase.waybase_template.format(waybase_info["label_offset"], self.label, waybase_info["location"])

        # Otherwise, set up the correct offsets for each label depending on the base reached (2nd, 3rd or home).
        elif self.end == 4 or self.end == "U":
            result += WayBase.waybase_template.format(waybase_info["number_offset"], self.number, waybase_info["location"] + "+(-1,-2)")
            result += WayBase.waybase_template.format(waybase_info["label_offset"], self.label, waybase_info["location"] + "+(-1,-5)")

        else:
            result += WayBase.waybase_template.format(waybase_info["label_offset"], self.label, waybase_info["location"])
            result += WayBase.waybase_template.format(waybase_info["number_offset"], self.number, waybase_info["location"] + "+(0,10)")

        return result
