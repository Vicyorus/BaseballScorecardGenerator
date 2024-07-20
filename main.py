#!/usr/bin/python3.10
from scorecard import Scorecard

game = Scorecard(
{
    "scorer": "Vicyorus",
    "date": "2018-08-14 19:08-21:48",
    "at": "Citizens Bank Park, Philadelphia, PA",
    "att": "33,081",
    "temp": "74F, Partly Cloudy",
    "wind": "7mph, Out To CF",
    "away": {
        "team": "Boston Red Sox",
        "starter": 22,
        "roster": {
            # Lineup
            50: "Mookie Betts",
            16: "Andrew Benintendi",
            18: "Mitch Moreland",
            28: "J.D. Martinez",
            2: "Xander Bogaerts",
            11: "Rafael Devers",
            36: "Eduardo Núñez",
            3: "Sandy León",
            # Starting pitcher
            22: "Rick Porcello",
            # Bench
            25: "Steve Pearce",
            12: "Brock Holt",
            23: "Blake Swihart",
            19: "Jackie Bradley Jr.",
            # Bullpen
            47: "Tyler Thornburg",
            41: "Chris Sale",
            31: "Drew Pomeranz",
            61: "Brian Johnson",
            37: "Heath Hembree",
            24: "David Price",
            46: "Craig Kimbrel",
            76: "Hector Velázquez",
            70: "Ryan Brasier",
            56: "Joe Kelly",
            17: "Nathan Eovaldi",
            32: "Matt Barnes",
        },
        "lefties": [41, 31, 61, 24],
        "lineup": [
            [50, "8"],
            [16, "7"],
            [18, "3"],
            [28, "9"],
            [2, "6"],
            [11, "5"],
            [36, "4"],
            [3, "2"],
            [22, "1"],
        ],
        "bench": [
            [25, "1B"],
            [12, "2B"],
            [23, "C"],
            [19, "CF"],
        ],
        "bullpen": [47, 41, 31, 61, 37, 24, 46, 76, 70, 56, 17, 32],
    },
    "home": {
        "team": "Philadelphia Phillies",
        "starter": 43,
        "roster": {
            # Lineup
            16: "César Hernández",
            5: "Nick Williams",
            13: "Asdrúbal Cabrera",
            17: "Rhys Hoskins",
            41: "Carlos Santana",
            7: "Maikel Franco",
            37: "Odúbel Herrera",
            38: "Jorge Alfaro",
            # Starting pitcher
            43: "Nick Pivetta",
            # Bench
            33: "Justin Bour",
            4: "Scott Kingery",
            15: "Andrew Knapp",
            24: "Roman Quinn",
            # Bullpen
            21: "Vince Velasquez",
            50: "Héctor Neris",
            47: "Aaron Loup",
            96: "Tommy Hunter",
            58: "Seranthony Domínguez",
            93: "Pat Neshek",
            49: "Jake Arrieta",
            64: "Víctor Arano",
            54: "Austin Davis",
            46: "Adam Morgan",
            27: "Aaron Nola",
            57: "Luis García",
        },
        "lefties": [47, 54, 46],
        "lineup": [
            [16, "4"],
            [5, "9"],
            [13, "6"],
            [17, "7"],
            [41, "3"],
            [7, "5"],
            [37, "8"],
            [38, "2"],
            [43, "1"],
        ],
        "bench": [
            [33, "1B"],
            [4, "SS"],
            [15, "C"],
            [24, "CF"],
        ],
        "bullpen": [21, 50, 47, 96, 58, 93, 49, 64, 54, 46, 27, 57],
    },
    "umpires": {
        "HP": "Will Little",
        "1B": "Kerwin Danley",
        "2B": "Ben May",
        "3B": "Ted Barrett",
    },
}
)

# Play ball!
t1 = game.new_inning(number=1)
b1 = game.new_inning(number=1, top=False)

t2 = game.new_inning(number=2)
b2 = game.new_inning(number=2, top=False)

t3 = game.new_inning(number=3)
b3 = game.new_inning(number=3, top=False)

t4 = game.new_inning(number=4)
b4 = game.new_inning(number=4, top=False)

t5 = game.new_inning(number=5)
b5 = game.new_inning(number=5, top=False)

t6 = game.new_inning(number=6)
b6 = game.new_inning(number=6, top=False)
# Offensive change (PHI): Pinch-hitter #24 Roman Quinn replaces #43 Nick Pivetta, batting 9th
b6.offensive_substitution(9, 24, 'PH')

t7 = game.new_inning(number=7)
# Pitching change (PHI): #93 Pat Neshek replaces #43 Nick Pivetta, batting 9th
t7.pitching_substitution(93)
t7.defensive_substitution(9, 93, 1)


b7 = game.new_inning(number=7, top=False)

t8 = game.new_inning(number=8)
# Pitching change (PHI): #96 Tommy Hunter replaces #93 Pat Neshek, batting 9th
t8.pitching_substitution(96)
t8.defensive_substitution(9, 96, 1)

# Offensive change (BOS): Pinch-hitter #12 Brock Holt replaces #22 Rick Porcello, batting 9th
t8.offensive_substitution(9, 12, 'PH')

b8 = game.new_inning(number=8, top=False)
# Pitching change (BOS): #37 Heath Hembree replaces #22 Rick Porcello, batting 9th
b8.pitching_substitution(37)
b8.defensive_substitution(9, 37, 1)


t9 = game.new_inning(number=9)
# Pitching change (PHI): #64 Víctor Arano replaces #96 Tommy Hunter, batting 9th
t9.pitching_substitution(64)
t9.defensive_substitution(9, 64, 1)


b9 = game.new_inning(number=9, top=False)
# Pitching change (BOS): #46 Craig Kimbrel replaces #37 Heath Hembree, batting 9th
b9.pitching_substitution(46)
b9.defensive_substitution(9, 46, 1)

# Offensive change (PHI): Pinch-hitter #33 Justin Bour replaces #64 Víctor Arano, batting 9th
b9.offensive_substitution(9, 33, 'PH')

# Offensive change (PHI): Pinch-runner #4 Scott Kingery replaces #33 Justin Bour
b9.offensive_substitution(9, 4, 'PR')

print(game)
