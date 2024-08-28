#!/usr/bin/python3.10
import os
from scorecard.scorecard import Scorecard

# BOS @ PHI, 2018-08-14
# https://www.baseball-reference.com/boxes/PHI/PHI201808140.shtml
# https://www.mlb.com/gameday/red-sox-vs-phillies/2018/08/14/531196/final

game = Scorecard(os.path.dirname(os.path.abspath(__file__)),
{
    "scorer": "Vicyorus",
    "date":   "2018-08-14 19:08-21:48",
    "at":     "Citizens Bank Park, Philadelphia, PA",
    "att":    "33,081",
    "temp":   "74F, Partly Cloudy",
    "wind":   "7mph, Out To CF",
    "away"   : {
        "team":    "Boston Red Sox",
        "starter": 22,
        "roster":  {
            # Lineup
            50 : "Mookie Betts",
            16 : "Andrew Benintendi",
            18 : "Mitch Moreland",
            28 : "J.D. Martinez",
            2  : "Xander Bogaerts",
            11 : "Rafael Devers",
            36 : "Eduardo Núñez",
            3  : "Sandy León",
            22 : "Rick Porcello",

            # Starting pitcher
            22 : "Rick Porcello",

            # Bench
            25 : "Steve Pearce",
            12 : "Brock Holt",
            23 : "Blake Swihart",
            19 : "Jackie Bradley Jr.",

            # Bullpen
            47 : "Tyler Thornburg",
            41 : "Chris Sale",
            31 : "Drew Pomeranz",
            61 : "Brian Johnson",
            37 : "Heath Hembree",
            24 : "David Price",
            46 : "Craig Kimbrel",
            76 : "Hector Velázquez",
            70 : "Ryan Brasier",
            56 : "Joe Kelly",
            17 : "Nathan Eovaldi",
            32 : "Matt Barnes",
        },
        "lefties" : [
            41, 31, 61, 24
        ],
        "lineup" : [
            [50, "8"],
            [16, "7"],
            [18, "3"],
            [28, "9"],
            [2,  "6"],
            [11, "5"],
            [36, "4"],
            [3,  "2"],
            [22, "1"],
        ],
        "bench" : [
            [25, "1B"],
            [12, "2B"],
            [23, "C" ],
            [19, "CF"],
        ],
        "bullpen" : [
            47, 41, 31, 61, 37, 24, 46, 76, 70, 56, 17, 32
        ],
    },
    "home"   : {
        "team":    "Philadelphia Phillies",
        "starter": 43,
        "roster":  {
            # Lineup
            16 : "César Hernández",
            5  : "Nick Williams",
            13 : "Asdrúbal Cabrera",
            17 : "Rhys Hoskins",
            41 : "Carlos Santana",
            7  : "Maikel Franco",
            37 : "Odúbel Herrera",
            38 : "Jorge Alfaro",
            43 : "Nick Pivetta",

            # Starting pitcher
            43 : "Nick Pivetta",

            # Bench
            33 : "Justin Bour",
            4  : "Scott Kingery",
            15 : "Andrew Knapp",
            24 : "Roman Quinn",

            # Bullpen
            21 : "Vince Velasquez",
            50 : "Héctor Neris",
            47 : "Aaron Loup",
            96 : "Tommy Hunter",
            58 : "Seranthony Domínguez",
            93 : "Pat Neshek",
            49 : "Jake Arrieta",
            64 : "Víctor Arano",
            54 : "Austin Davis",
            46 : "Adam Morgan",
            27 : "Aaron Nola",
            57 : "Luis García",
        },
        "lefties" : [
            47, 54, 46
        ],
        "lineup" : [
            [16, "4"],
            [5,  "9"],
            [13, "6"],
            [17, "7"],
            [41, "3"],
            [7,  "5"],
            [37, "8"],
            [38, "2"],
            [43, "1"],
        ],
        "bench" : [
            [33, "1B"],
            [4,  "SS"],
            [15, "C" ],
            [24, "CF"],
        ],
        "bullpen" : [
            21, 50, 47, 96, 58, 93, 49, 64, 54, 46, 27, 57
        ],
    },
    "umpires" : {
        "HP" : "Will Little",
        "1B" : "Kerwin Danley",
        "2B" : "Ben May",
        "3B" : "Ted Barrett",
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
inn = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
inn.new_ab()
inn.out("P3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
inn.new_ab()
inn.pitch_list("b f f f b f b f f s")
inn.out("K")

# 3. BOS #18 Mitch Moreland (X - X - X)
inn.new_ab()
inn.out("G4-3")


# Bot 1st
# Pitching: BOS #22 Rick Porcello
inn = game.new_inning()

# 1. PHI #16 César Hernández (X - X - X)
inn.new_ab()
inn.pitch_list("c b c c")
inn.out("!K")

# 2. PHI #5  Nick Williams (X - X - X)
inn.new_ab()
inn.out("G6-3")

# 3. PHI #13 Asdrúbal Cabrera (X - X - X)
inn.new_ab()
inn.pitch_list("c b f b s")
inn.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: PHI #43 Nick Pivetta
inn = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
inn.new_ab()
inn.pitch_list("c b")
inn.hit(1)
inn.thrown_out(2, "2 DP5-4-3", 1, 43)

# 5. BOS #2  Xander Bogaerts (X - X - 28)
inn.new_ab()
inn.pitch_list("c b f f")
inn.out("DP5-4-3")

# 6. BOS #11 Rafael Devers (X - X - X)
inn.new_ab()
inn.pitch_list("c s s")
inn.out("K")


# Bot 2nd
# Pitching: BOS #22 Rick Porcello
inn = game.new_inning()

# 4. PHI #17 Rhys Hoskins (X - X - X)
inn.new_ab()
inn.pitch_list("c b b")
inn.out("F7")

# 5. PHI #41 Carlos Santana (X - X - X)
inn.new_ab()
inn.pitch_list("c f b f b c")
inn.out("!K")

# 6. PHI #7  Maikel Franco (X - X - X)
inn.new_ab()
inn.pitch_list("b")
inn.out("F8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: PHI #43 Nick Pivetta
inn = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
inn.new_ab()
inn.pitch_list("c b b f s")
inn.out("K")

# 8. BOS #3  Sandy León (X - X - X)
inn.new_ab()
inn.pitch_list("c b b")
inn.hit(4, rbis=1)

# 9. BOS #22 Rick Porcello (X - X - X)
inn.new_ab()
inn.hit(2)

# 1. BOS #50 Mookie Betts (X - 22 - X)
inn.new_ab()
inn.pitch_list("c s b b d d")
inn.reach('BB')
inn.thrown_out(2, "16 DP4-6-3", 2, 43)

# 2. BOS #16 Andrew Benintendi (X - 22 - 50)
inn.new_ab()
inn.pitch_list("c b c f f f b f b")
inn.out("DP4-6-3")


# Bot 3rd
# Pitching: BOS #22 Rick Porcello
inn = game.new_inning()

# 7. PHI #37 Odúbel Herrera (X - X - X)
inn.new_ab()
inn.pitch_list("c f b f b b")
inn.out("G4-3")

# 8. PHI #38 Jorge Alfaro (X - X - X)
inn.new_ab()
inn.pitch_list("c s b c")
inn.out("!K")

# 9. PHI #43 Nick Pivetta (X - X - X)
inn.new_ab()
inn.pitch_list("c b c s")
inn.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: PHI #43 Nick Pivetta
inn = game.new_inning()

# 3. BOS #18 Mitch Moreland (X - X - X)
inn.new_ab()
inn.out("(F)P5")

# 4. BOS #28 J.D. Martinez (X - X - X)
inn.new_ab()
inn.pitch_list("c c b s")
inn.out("K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
inn.new_ab()
inn.pitch_list("s")
inn.error(5)
inn.reach('E5')

# 6. BOS #11 Rafael Devers (X - X - 2)
inn.new_ab()
inn.pitch_list("b c s 1 f s")
inn.out("K")


# Bot 4th
# Pitching: BOS #22 Rick Porcello
inn = game.new_inning()

# 1. PHI #16 César Hernández (X - X - X)
inn.new_ab()
inn.pitch_list("b")
inn.out("G3-1")

# 2. PHI #5  Nick Williams (X - X - X)
inn.new_ab()
inn.pitch_list("c b s b f s")
inn.out("K")

# 3. PHI #13 Asdrúbal Cabrera (X - X - X)
inn.new_ab()
inn.pitch_list("c s c")
inn.out("!K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: PHI #43 Nick Pivetta
inn = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
inn.new_ab()
inn.pitch_list("s")
inn.out("F7")

# 8. BOS #3  Sandy León (X - X - X)
inn.new_ab()
inn.pitch_list("c b f")
inn.out("G4-3")

# 9. BOS #22 Rick Porcello (X - X - X)
inn.new_ab()
inn.pitch_list("c f b s")
inn.out("K")


# Bot 5th
# Pitching: BOS #22 Rick Porcello
inn = game.new_inning()

# 4. PHI #17 Rhys Hoskins (X - X - X)
inn.new_ab()
inn.pitch_list("c b")
inn.hit(4, rbis=1)

# 5. PHI #41 Carlos Santana (X - X - X)
inn.new_ab()
inn.pitch_list("c b f")
inn.out("G4-3")

# 6. PHI #7  Maikel Franco (X - X - X)
inn.new_ab()
inn.pitch_list("c b b b f")
inn.out("G3-1")

# 7. PHI #37 Odúbel Herrera (X - X - X)
inn.new_ab()
inn.pitch_list("c f")
inn.hit(1)

# 8. PHI #38 Jorge Alfaro (X - X - 37)
inn.new_ab()
inn.pitch_list("b c f f")
inn.out("G1-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: PHI #43 Nick Pivetta
inn = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
inn.new_ab()
inn.pitch_list("c b s")
inn.out("L9")

# 2. BOS #16 Andrew Benintendi (X - X - X)
inn.new_ab()
inn.pitch_list("c t f b b")
inn.out("L3")

# 3. BOS #18 Mitch Moreland (X - X - X)
inn.new_ab()
inn.pitch_list("b c")
inn.out("F8")


# Bot 6th
# Pitching: BOS #22 Rick Porcello
inn = game.new_inning()

# Offensive change (PHI): Pinch-hitter #24 Roman Quinn replaces #43 Nick Pivetta, batting 9th
inn.offensive_substitution(9, 24, "PH")

# 9. PHI #24 Roman Quinn (X - X - X)
inn.new_ab()
inn.out("F7")

# 1. PHI #16 César Hernández (X - X - X)
inn.new_ab()
inn.pitch_list("b c s s")
inn.out("K")

# 2. PHI #5  Nick Williams (X - X - X)
inn.new_ab()
inn.pitch_list("c f b b s")
inn.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: PHI #93 Pat Neshek
inn = game.new_inning()

# Pitching change (PHI): #93 Pat Neshek replaces #43 Nick Pivetta, batting 9th
inn.pitching_substitution(93)
inn.defensive_substitution(9, 93, "1")

# 4. BOS #28 J.D. Martinez (X - X - X)
inn.new_ab()
inn.pitch_list("c b f s")
inn.out("K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
inn.new_ab()
inn.pitch_list("s s b")
inn.out("L9")

# 6. BOS #11 Rafael Devers (X - X - X)
inn.new_ab()
inn.pitch_list("b b c b f f b")
inn.reach('BB')

# 7. BOS #36 Eduardo Núñez (X - X - 11)
inn.new_ab()
inn.out("L9")


# Bot 7th
# Pitching: BOS #22 Rick Porcello
inn = game.new_inning()

# 3. PHI #13 Asdrúbal Cabrera (X - X - X)
inn.new_ab()
inn.pitch_list("c")
inn.out("F7")

# 4. PHI #17 Rhys Hoskins (X - X - X)
inn.new_ab()
inn.pitch_list("b b c")
inn.out("F9")

# 5. PHI #41 Carlos Santana (X - X - X)
inn.new_ab()
inn.pitch_list("s b f b s")
inn.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: PHI #96 Tommy Hunter
inn = game.new_inning()

# Pitching change (PHI): #96 Tommy Hunter replaces #93 Pat Neshek, batting 9th
inn.pitching_substitution(96)
inn.defensive_substitution(9, 96, "1")

# 8. BOS #3  Sandy León (X - X - X)
inn.new_ab()
inn.pitch_list("b f f c")
inn.out("!K")

# Offensive change (BOS): Pinch-hitter #12 Brock Holt replaces #22 Rick Porcello, batting 9th
inn.offensive_substitution(9, 12, "PH")

# 9. BOS #12 Brock Holt (X - X - X)
inn.new_ab()
inn.hit(4, rbis=1)

# 1. BOS #50 Mookie Betts (X - X - X)
inn.new_ab()
inn.pitch_list("b f")
inn.hit(2)
inn.advance(3, '18 SB')

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
inn.new_ab()
inn.out("F7")

# 3. BOS #18 Mitch Moreland (X - 50 - X)
inn.new_ab()
inn.pitch_list("b b f s b")
inn.out("F7")


# Bot 8th
# Pitching: BOS #37 Heath Hembree
inn = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #22 Rick Porcello, batting 9th
inn.pitching_substitution(37)
inn.defensive_substitution(9, 37, "1")

# 6. PHI #7  Maikel Franco (X - X - X)
inn.new_ab()
inn.pitch_list("b c b f")
inn.out("G1-3")

# 7. PHI #37 Odúbel Herrera (X - X - X)
inn.new_ab()
inn.pitch_list("f s b b f s")
inn.out("K")

# 8. PHI #38 Jorge Alfaro (X - X - X)
inn.new_ab()
inn.pitch_list("f b b b f f c")
inn.out("!K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: PHI #64 Víctor Arano
inn = game.new_inning()

# Pitching change (PHI): #64 Víctor Arano replaces #96 Tommy Hunter, batting 9th
inn.pitching_substitution(64)
inn.defensive_substitution(9, 64, "1")

# 4. BOS #28 J.D. Martinez (X - X - X)
inn.new_ab()
inn.pitch_list("c b b b c")
inn.out("G5-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
inn.new_ab()
inn.pitch_list("b c")
inn.hit(1)
inn.thrown_out(2, "36 FC4", 3, 64)

# 6. BOS #11 Rafael Devers (X - X - 2)
inn.new_ab()
inn.pitch_list("1 f 1 f")
inn.out("L7")

# 7. BOS #36 Eduardo Núñez (X - X - 2)
inn.new_ab()
inn.pitch_list("1 1 d")
inn.reach('FC4')


# Bot 9th
# Pitching: BOS #46 Craig Kimbrel
inn = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #37 Heath Hembree, batting 9th
inn.pitching_substitution(46)
inn.defensive_substitution(9, 46, "1")

# Offensive change (PHI): Pinch-hitter #33 Justin Bour replaces #64 Víctor Arano, batting 9th
inn.offensive_substitution(9, 33, "PH")

# 9. PHI #33 Justin Bour (X - X - X)
inn.new_ab()
inn.pitch_list("s b b f b b")
inn.reach('BB')
# Offensive change (PHI): Pinch-runner #4 Scott Kingery replaces #33 Justin Bour
inn.offensive_substitution(9, 4, "PR")
inn.atbase("PR")
inn.advance(2, '13 SB')

# 1. PHI #16 César Hernández (X - X - 33)
inn.new_ab()
inn.pitch_list("b 1 c 1")
inn.out("F7")

# 2. PHI #5  Nick Williams (X - X - 4)
inn.new_ab()
inn.pitch_list("s f 1 1")
inn.out("L6")

# 3. PHI #13 Asdrúbal Cabrera (X - X - 4)
inn.new_ab()
inn.pitch_list("b c s f b s")
inn.out("K2-3")

# Winning team: BOS
# WP: BOS #22 Rick Porcello
game.winning_pitcher(22, is_away_team=True)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46, is_away_team=True)

# Loser team: PHI
# LP: PHI #96 Tommy Hunter
game.losing_pitcher(96)

#print(game)
game.generate_scorecard()
