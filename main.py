#!/usr/bin/python3.10
from scorecard import Scorecard

# BOS @ PHI, 2018-08-14
# https://www.baseball-reference.com/boxes/PHI/PHI201808140.shtml
# https://www.mlb.com/gameday/red-sox-vs-phillies/2018/08/14/531196/final

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

##########################################################
# PLAY BALL!
##########################################################


##########################################################
# 1st Inning
##########################################################
# Top 1st
# Pitching: PHI #43 Nick Pivetta
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.out('P3')

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("b f f f b f b f f")
t1.out('K')

# 3. BOS #18 Mitch Moreland (X - X - X)
t1.new_ab()
t1.out('G4-3')


# Bot 1st
# Pitching: BOS #22 Rick Porcello
b1 = game.new_inning()

# 1. PHI #16 César Hernández (X - X - X)
b1.new_ab()
b1.pitch_list("c b c")
b1.out('!K')

# 2. PHI #5  Nick Williams (X - X - X)
b1.new_ab()
b1.out('G6-3')

# 3. PHI #13 Asdrúbal Cabrera (X - X - X)
b1.new_ab()
b1.pitch_list("c b f b")
b1.out('K')


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: PHI #43 Nick Pivetta
t2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.hit(1)
t2.thrown_out(2, '2 DP5-4-3', 1, 43)

# 5. BOS #2  Xander Bogaerts (X - X - 28)
t2.new_ab()
t2.pitch_list("c b f f")
t2.out('DP5-4-3')

# 6. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.pitch_list("c s")
t2.out('K')


# Bot 2nd
# Pitching: BOS #22 Rick Porcello
b2 = game.new_inning()

# 4. PHI #17 Rhys Hoskins (X - X - X)
b2.new_ab()
b2.pitch_list("c b b")
b2.out('F7')

# 5. PHI #41 Carlos Santana (X - X - X)
b2.new_ab()
b2.pitch_list("c f b f b")
b2.out('!K')

# 6. PHI #7  Maikel Franco (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out('F8')


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: PHI #43 Nick Pivetta
t3 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
t3.new_ab()
t3.pitch_list("c b b f")
t3.out('K')

# 8. BOS #3  Sandy León (X - X - X)
t3.new_ab()
t3.pitch_list("c b b")
t3.hit(4)

# 9. BOS #22 Rick Porcello (X - X - X)
t3.new_ab()
t3.hit(2)

# 1. BOS #50 Mookie Betts (X - 22 - X)
t3.new_ab()
t3.pitch_list("c s b b d")
t3.reach('BB')
t3.thrown_out(2, '16 DP4-6-3', 2, 43)

# 2. BOS #16 Andrew Benintendi (X - 22 - 50)
t3.new_ab()
t3.pitch_list("c b c f f f b f b")
t3.out('DP4-6-3')


# Bot 3rd
# Pitching: BOS #22 Rick Porcello
b3 = game.new_inning()

# 7. PHI #37 Odúbel Herrera (X - X - X)
b3.new_ab()
b3.pitch_list("c f b f b b")
b3.out('G4-3')

# 8. PHI #38 Jorge Alfaro (X - X - X)
b3.new_ab()
b3.pitch_list("c s b")
b3.out('!K')

# 9. PHI #43 Nick Pivetta (X - X - X)
b3.new_ab()
b3.pitch_list("c b c")
b3.out('K')


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: PHI #43 Nick Pivetta
t4 = game.new_inning()

# 3. BOS #18 Mitch Moreland (X - X - X)
t4.new_ab()
t4.out('(F)P5')

# 4. BOS #28 J.D. Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("c c b")
t4.out('K')

# 5. BOS #2  Xander Bogaerts (X - X - X)
t4.new_ab()
t4.pitch_list("s")
t4.error(5)
t4.reach('E5')

# 6. BOS #11 Rafael Devers (X - X - 2)
t4.new_ab()
t4.pitch_list("b c s 1 f")
t4.out('K')


# Bot 4th
# Pitching: BOS #22 Rick Porcello
b4 = game.new_inning()

# 1. PHI #16 César Hernández (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out('G3-1')

# 2. PHI #5  Nick Williams (X - X - X)
b4.new_ab()
b4.pitch_list("c b s b f")
b4.out('K')

# 3. PHI #13 Asdrúbal Cabrera (X - X - X)
b4.new_ab()
b4.pitch_list("c s")
b4.out('!K')


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: PHI #43 Nick Pivetta
t5 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
t5.new_ab()
t5.pitch_list("s")
t5.out('F7')

# 8. BOS #3  Sandy León (X - X - X)
t5.new_ab()
t5.pitch_list("c b f")
t5.out('G4-3')

# 9. BOS #22 Rick Porcello (X - X - X)
t5.new_ab()
t5.pitch_list("c f b")
t5.out('K')


# Bot 5th
# Pitching: BOS #22 Rick Porcello
b5 = game.new_inning()

# 4. PHI #17 Rhys Hoskins (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.hit(4)

# 5. PHI #41 Carlos Santana (X - X - X)
b5.new_ab()
b5.pitch_list("c b f")
b5.out('G4-3')

# 6. PHI #7  Maikel Franco (X - X - X)
b5.new_ab()
b5.pitch_list("c b b b f")
b5.out('G3-1')

# 7. PHI #37 Odúbel Herrera (X - X - X)
b5.new_ab()
b5.pitch_list("c f")
b5.hit(1)

# 8. PHI #38 Jorge Alfaro (X - X - 37)
b5.new_ab()
b5.pitch_list("b c f f")
b5.out('G1-3')


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: PHI #43 Nick Pivetta
t6 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t6.new_ab()
t6.pitch_list("c b s")
t6.out('L9')

# 2. BOS #16 Andrew Benintendi (X - X - X)
t6.new_ab()
t6.pitch_list("c t f b b")
t6.out('L3')

# 3. BOS #18 Mitch Moreland (X - X - X)
t6.new_ab()
t6.pitch_list("b c")
t6.out('F8')


# Bot 6th
# Pitching: BOS #22 Rick Porcello
b6 = game.new_inning()

# Offensive substitution (PHI): Pinch-hitter #24 Roman Quinn replaces #43 Nick Pivetta, batting 9th
b6.offensive_substitution(9, 24, 'PH')

# 9. PHI #24 Roman Quinn (X - X - X)
b6.new_ab()
b6.out('F7')

# 1. PHI #16 César Hernández (X - X - X)
b6.new_ab()
b6.pitch_list("b c s")
b6.out('K')

# 2. PHI #5  Nick Williams (X - X - X)
b6.new_ab()
b6.pitch_list("c f b b")
b6.out('K')


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: PHI #93 Pat Neshek
t7 = game.new_inning()

# Pitching substitution (PHI): #93 Pat Neshek replaces #43 Nick Pivetta, batting 9th
t7.pitching_substitution(93)
t7.defensive_substitution(9, 93, 1)

# 4. BOS #28 J.D. Martinez (X - X - X)
t7.new_ab()
t7.pitch_list("c b f")
t7.out('K')

# 5. BOS #2  Xander Bogaerts (X - X - X)
t7.new_ab()
t7.pitch_list("s s b")
t7.out('L9')

# 6. BOS #11 Rafael Devers (X - X - X)
t7.new_ab()
t7.pitch_list("b b c b f f")
t7.reach('BB')

# 7. BOS #36 Eduardo Núñez (X - X - 11)
t7.new_ab()
t7.out('L9')


# Bot 7th
# Pitching: BOS #22 Rick Porcello
b7 = game.new_inning()

# 3. PHI #13 Asdrúbal Cabrera (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out('F7')

# 4. PHI #17 Rhys Hoskins (X - X - X)
b7.new_ab()
b7.pitch_list("b b c")
b7.out('F9')

# 5. PHI #41 Carlos Santana (X - X - X)
b7.new_ab()
b7.pitch_list("s b f b")
b7.out('K')


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: PHI #96 Tommy Hunter
t8 = game.new_inning()

# Pitching substitution (PHI): #96 Tommy Hunter replaces #93 Pat Neshek, batting 9th
t8.pitching_substitution(96)
t8.defensive_substitution(9, 96, 1)

# 8. BOS #3  Sandy León (X - X - X)
t8.new_ab()
t8.pitch_list("b f f")
t8.out('!K')

# Offensive substitution (BOS): Pinch-hitter #12 Brock Holt replaces #22 Rick Porcello, batting 9th
t8.offensive_substitution(9, 12, 'PH')

# 9. BOS #12 Brock Holt (X - X - X)
t8.new_ab()
t8.hit(4)

# 1. BOS #50 Mookie Betts (X - X - X)
t8.new_ab()
t8.pitch_list("b f")
t8.hit(2)
t8.advance(3, '18 SB')

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
t8.new_ab()
t8.out('F7')

# 3. BOS #18 Mitch Moreland (X - 50 - X)
t8.new_ab()
t8.pitch_list("b b f s b")
t8.out('F7')


# Bot 8th
# Pitching: BOS #37 Heath Hembree
b8 = game.new_inning()

# Pitching substitution (BOS): #37 Heath Hembree replaces #22 Rick Porcello, batting 9th
b8.pitching_substitution(37)
b8.defensive_substitution(9, 37, 1)

# 6. PHI #7  Maikel Franco (X - X - X)
b8.new_ab()
b8.pitch_list("b c b f")
b8.out('G1-3')

# 7. PHI #37 Odúbel Herrera (X - X - X)
b8.new_ab()
b8.pitch_list("f s b b f")
b8.out('K')

# 8. PHI #38 Jorge Alfaro (X - X - X)
b8.new_ab()
b8.pitch_list("f b b b f f")
b8.out('!K')


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: PHI #64 Víctor Arano
t9 = game.new_inning()

# Pitching substitution (PHI): #64 Víctor Arano replaces #96 Tommy Hunter, batting 9th
t9.pitching_substitution(64)
t9.defensive_substitution(9, 64, 1)

# 4. BOS #28 J.D. Martinez (X - X - X)
t9.new_ab()
t9.pitch_list("c b b b c")
t9.out('G5-3')

# 5. BOS #2  Xander Bogaerts (X - X - X)
t9.new_ab()
t9.pitch_list("b c")
t9.hit(1)
t9.thrown_out(2, '36 FC4', 3, 64)

# 6. BOS #11 Rafael Devers (X - X - 2)
t9.new_ab()
t9.pitch_list("1 f 1 f")
t9.out('L7')

# 7. BOS #36 Eduardo Núñez (X - X - 2)
t9.new_ab()
t9.pitch_list("1 1 d")
t9.reach('FC4')


# Bot 9th
# Pitching: BOS #46 Craig Kimbrel
b9 = game.new_inning()

# Pitching substitution (BOS): #46 Craig Kimbrel replaces #37 Heath Hembree, batting 9th
b9.pitching_substitution(46)
b9.defensive_substitution(9, 46, 1)

# Offensive substitution (PHI): Pinch-hitter #33 Justin Bour replaces #64 Víctor Arano, batting 9th
b9.offensive_substitution(9, 33, 'PH')

# 9. PHI #33 Justin Bour (X - X - X)
b9.new_ab()
b9.pitch_list("s b b f b")
b9.reach('BB')
# Offensive substitution (PHI): Pinch-runner #4 Scott Kingery replaces #33 Justin Bour
b9.offensive_substitution(9, 4, 'PR')
b9.atbase('PR')
b9.advance(2, '13 SB')

# 1. PHI #16 César Hernández (X - X - 33)
b9.new_ab()
b9.pitch_list("b 1 c 1")
b9.out('F7')

# 2. PHI #5  Nick Williams (X - X - 4)
b9.new_ab()
b9.pitch_list("s f 1 1")
b9.out('L6')

# 3. PHI #13 Asdrúbal Cabrera (X - X - 4)
b9.new_ab()
b9.pitch_list("b c s f b")
b9.out('K2-3')

print(game)
