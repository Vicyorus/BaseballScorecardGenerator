#!/usr/bin/python3.10
import os
from scorecard.scorecard import Scorecard

# NYY @ BOS, 2018-08-03
# https://www.baseball-reference.com/boxes/BOS/BOS201808030.shtml
# https://www.mlb.com/gameday/yankees-vs-red-sox/2018/08/03/531059/final

game = Scorecard(os.path.dirname(os.path.abspath(__file__)),
{
    "scorer": "Vicyorus",
    "date":   "2018-08-03 19:10-21:25",
    "at":     "Fenway Park, Boston, MA",
    "att":    "37,231",
    "temp":   "87F, Partly Cloudy",
    "wind":   "21mph, Out To CF",
    "away"   : {
        "team":    "New York Yankees",
        "starter": 40,
        "roster":  {
            # Lineup
            11 : "Brett Gardner",
            27 : "Giancarlo Stanton",
            18 : "Didi Gregorius",
            31 : "Aaron Hicks",
            25 : "Gleyber Torres",
            33 : "Greg Bird",
            41 : "Miguel Andujar",
            28 : "Austin Romine",
            14 : "Neil Walker",

            # Starting pitcher
            40 : "Luis Severino",

            # Bench
            66 : "Kyle Higashioka",
            38 : "Shane Robinson",
            45 : "Luke Voit",

            # Bullpen
            67 : "A.J. Cole",
            68 : "Dellin Betances",
            36 : "Lance Lynn",
            55 : "Sonny Gray",
            56 : "Jonathan Holder",
            52 : "CC Sabathia",
            53 : "Zack Britton",
            19 : "Masahiro Tanaka",
            57 : "Chad Green",
            48 : "Tommy Kahnle",
            30 : "David Robertson",
            54 : "Aroldis Chapman",
        },
        "lefties" : [
            52, 53, 54
        ],
        "lineup" : [
            [11, "7"],
            [27, "9"],
            [18, "6"],
            [31, "8"],
            [25, "4"],
            [33, "3"],
            [41, "0"],
            [28, "2"],
            [14, "5"],
        ],
        "bench" : [
            [66, "C" ],
            [38, "CF"],
            [45, "1B"],
        ],
        "bullpen" : [
            67, 68, 36, 55, 56, 52, 53, 19, 57, 48, 30, 54
        ],
    },
    "home"   : {
        "team":    "Boston Red Sox",
        "starter": 22,
        "roster":  {
            # Lineup
            50 : "Mookie Betts",
            16 : "Andrew Benintendi",
            25 : "Steve Pearce",
            28 : "J.D. Martinez",
            5  : "Ian Kinsler",
            36 : "Eduardo Núñez",
            12 : "Brock Holt",
            3  : "Sandy León",
            19 : "Jackie Bradley Jr.",

            # Starting pitcher
            22 : "Rick Porcello",

            # Bench
            18 : "Mitch Moreland",
            68 : "Dan Butler",
            2  : "Xander Bogaerts",

            # Bullpen
            47 : "Tyler Thornburg",
            44 : "Brandon Workman",
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
            31, 61, 24
        ],
        "lineup" : [
            [50, "9"],
            [16, "7"],
            [25, "3"],
            [28, "0"],
            [5,  "4"],
            [36, "5"],
            [12, "6"],
            [3,  "2"],
            [19, "8"],
        ],
        "bench" : [
            [18, "1B"],
            [68, "C" ],
            [2,  "2B"],
        ],
        "bullpen" : [
            47, 44, 31, 61, 37, 24, 46, 76, 70, 56, 17, 32
        ],
    },
    "umpires" : {
        "HP" : "Adam Hamari",
        "1B" : "Phil Cuzzi",
        "2B" : "Chris Conroy",
        "3B" : "Dan Bellino",
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
# Pitching: BOS #22 Rick Porcello
inn = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
inn.new_ab()
inn.pitch_list("c c")
inn.reach('HBP')
inn.thrown_out(2, "27 DP4-6-3", 1, 22)

# 2. NYY #27 Giancarlo Stanton (X - X - 11)
inn.new_ab()
inn.pitch_list("c 1 f")
inn.out("DP4-6-3")

# 3. NYY #18 Didi Gregorius (X - X - X)
inn.new_ab()
inn.pitch_list("c f f f b f")
inn.out("P5")


# Bot 1st
# Pitching: NYY #40 Luis Severino
inn = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
inn.new_ab()
inn.pitch_list("b c b c f")
inn.out("G5-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
inn.new_ab()
inn.pitch_list("f b f")
inn.hit(2)
inn.advance(4, '25 HR')

# 3. BOS #25 Steve Pearce (X - 16 - X)
inn.new_ab()
inn.pitch_list("b")
inn.hit(4, rbis=2)

# 4. BOS #28 J.D. Martinez (X - X - X)
inn.new_ab()
inn.pitch_list("b b c s f")
inn.out("F9")

# 5. BOS #5  Ian Kinsler (X - X - X)
inn.new_ab()
inn.pitch_list("b c f b b b")
inn.reach('BB')
inn.advance(2, '36 SB')
inn.advance(4, '36 1B')

# 6. BOS #36 Eduardo Núñez (X - X - 5)
inn.new_ab()
inn.pitch_list("b c b")
inn.hit(1, rbis=1)

# 7. BOS #12 Brock Holt (X - X - 36)
inn.new_ab()
inn.pitch_list("1 b c b 1 f")
inn.out("L8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Rick Porcello
inn = game.new_inning()

# Defensive switch (BOS): #50 Mookie Betts moves to 2B
inn.defensive_switch(50, "4")

# Defensive switch (BOS): #25 Steve Pearce moves to RF
inn.defensive_switch(25, "9")

# Defensive change (BOS): #18 Mitch Moreland replaces #5 Ian Kinsler (2B), playing 1B, batting 5th
inn.defensive_substitution(5, 18, "3")

# 4. NYY #31 Aaron Hicks (X - X - X)
inn.new_ab()
inn.pitch_list("b c c b")
inn.out("G4-3")

# 5. NYY #25 Gleyber Torres (X - X - X)
inn.new_ab()
inn.pitch_list("b")
inn.out("(F)P2")

# 6. NYY #33 Greg Bird (X - X - X)
inn.new_ab()
inn.pitch_list("c c s")
inn.out("K")


# Bot 2nd
# Pitching: NYY #40 Luis Severino
inn = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
inn.new_ab()
inn.pitch_list("s b c")
inn.out("F8")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
inn.new_ab()
inn.pitch_list("b f b s b c")
inn.out("!K")

# 1. BOS #50 Mookie Betts (X - X - X)
inn.new_ab()
inn.pitch_list("s")
inn.hit(2)

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
inn.new_ab()
inn.pitch_list("b b f b d")
inn.reach('BB')
inn.thrown_out(2, "25 FC6-4", 3, 40)

# 3. BOS #25 Steve Pearce (X - 50 - 16)
inn.new_ab()
inn.pitch_list("f")
inn.reach('FC6-4')


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Rick Porcello
inn = game.new_inning()

# 7. NYY #41 Miguel Andujar (X - X - X)
inn.new_ab()
inn.pitch_list("c")
inn.hit(4, rbis=1)

# 8. NYY #28 Austin Romine (X - X - X)
inn.new_ab()
inn.out("G3-1")

# 9. NYY #14 Neil Walker (X - X - X)
inn.new_ab()
inn.pitch_list("c b f c")
inn.out("!K")

# 1. NYY #11 Brett Gardner (X - X - X)
inn.new_ab()
inn.pitch_list("c b f c")
inn.out("!K")


# Bot 3rd
# Pitching: NYY #40 Luis Severino
inn = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
inn.new_ab()
inn.pitch_list("f s b f b")
inn.out("G5-3")

# 5. BOS #18 Mitch Moreland (X - X - X)
inn.new_ab()
inn.hit(1)
inn.thrown_out(2, "36 FC5-4", 2, 40)

# 6. BOS #36 Eduardo Núñez (X - X - 18)
inn.new_ab()
inn.pitch_list("b b f f")
inn.reach('FC5-4')

# 7. BOS #12 Brock Holt (X - X - 36)
inn.new_ab()
inn.pitch_list("1 f f")
inn.out("G4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #22 Rick Porcello
inn = game.new_inning()

# 2. NYY #27 Giancarlo Stanton (X - X - X)
inn.new_ab()
inn.pitch_list("c s")
inn.out("L8")

# 3. NYY #18 Didi Gregorius (X - X - X)
inn.new_ab()
inn.pitch_list("c")
inn.out("L8")

# 4. NYY #31 Aaron Hicks (X - X - X)
inn.new_ab()
inn.pitch_list("s b b")
inn.out("L8")


# Bot 4th
# Pitching: NYY #40 Luis Severino
inn = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
inn.new_ab()
inn.pitch_list("c b b f f")
inn.out("G6-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
inn.new_ab()
inn.pitch_list("b c b b f f f c")
inn.out("!K")

# 1. BOS #50 Mookie Betts (X - X - X)
inn.new_ab()
inn.pitch_list("b f")
inn.out("L8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #22 Rick Porcello
inn = game.new_inning()

# 5. NYY #25 Gleyber Torres (X - X - X)
inn.new_ab()
inn.pitch_list("c c s")
inn.out("K")

# 6. NYY #33 Greg Bird (X - X - X)
inn.new_ab()
inn.pitch_list("c s t")
inn.out("KT")

# 7. NYY #41 Miguel Andujar (X - X - X)
inn.new_ab()
inn.pitch_list("c")
inn.out("F7")


# Bot 5th
# Pitching: NYY #40 Luis Severino
inn = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
inn.new_ab()
inn.pitch_list("c b c")
inn.out("F8")

# 3. BOS #25 Steve Pearce (X - X - X)
inn.new_ab()
inn.pitch_list("b f b b")
inn.out("L7")

# 4. BOS #28 J.D. Martinez (X - X - X)
inn.new_ab()
inn.pitch_list("c c b")
inn.hit(2)
inn.advance(4, '18 1B')

# 5. BOS #18 Mitch Moreland (X - 28 - X)
inn.new_ab()
inn.pitch_list("c")
inn.hit(1, rbis=1)

# 6. BOS #36 Eduardo Núñez (X - X - 18)
inn.new_ab()
inn.pitch_list("c")
inn.out("P6")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #22 Rick Porcello
inn = game.new_inning()

# 8. NYY #28 Austin Romine (X - X - X)
inn.new_ab()
inn.pitch_list("b c")
inn.out("G4-3")

# 9. NYY #14 Neil Walker (X - X - X)
inn.new_ab()
inn.pitch_list("f b f b t")
inn.out("KT")

# 1. NYY #11 Brett Gardner (X - X - X)
inn.new_ab()
inn.pitch_list("b")
inn.out("G3")


# Bot 6th
# Pitching: NYY #40 Luis Severino
inn = game.new_inning()

# 7. BOS #12 Brock Holt (X - X - X)
inn.new_ab()
inn.pitch_list("c")
inn.out("L9")

# 8. BOS #3  Sandy León (X - X - X)
inn.new_ab()
inn.pitch_list("b f")
inn.out("G5-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
inn.new_ab()
inn.pitch_list("c b f b b f f f b")
inn.reach('BB')
inn.thrown_out(2, "50 FC6-4", 3, 30)

# Pitching change (NYY): #30 David Robertson replaces #40 Luis Severino
inn.pitching_substitution(30)

# 1. BOS #50 Mookie Betts (X - X - 19)
inn.new_ab()
inn.pitch_list("1 b")
inn.reach('FC6-4')


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #22 Rick Porcello
inn = game.new_inning()

# 2. NYY #27 Giancarlo Stanton (X - X - X)
inn.new_ab()
inn.pitch_list("s f c")
inn.out("!K")

# 3. NYY #18 Didi Gregorius (X - X - X)
inn.new_ab()
inn.pitch_list("b f f s")
inn.out("K")

# 4. NYY #31 Aaron Hicks (X - X - X)
inn.new_ab()
inn.out("G3")


# Bot 7th
# Pitching: NYY #30 David Robertson
inn = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
inn.new_ab()
inn.out("G3-1")

# 3. BOS #25 Steve Pearce (X - X - X)
inn.new_ab()
inn.pitch_list("b b s b b")
inn.reach('BB')
inn.thrown_out(2, "28 DP6-4-3", 2, 30)

# 4. BOS #28 J.D. Martinez (X - X - 25)
inn.new_ab()
inn.pitch_list("d f c")
inn.out("DP6-4-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #22 Rick Porcello
inn = game.new_inning()

# Defensive switch (BOS): #50 Mookie Betts moves to RF
inn.defensive_switch(50, "9")

# Defensive change (BOS): #2 Xander Bogaerts replaces #25 Steve Pearce (1B), playing SS, batting 3rd
inn.defensive_substitution(3, 2, "6")

# Defensive switch (BOS): #12 Brock Holt moves to 2B
inn.defensive_switch(12, "4")

# 5. NYY #25 Gleyber Torres (X - X - X)
inn.new_ab()
inn.pitch_list("c b b f f s")
inn.out("K")

# 6. NYY #33 Greg Bird (X - X - X)
inn.new_ab()
inn.out("F8")

# 7. NYY #41 Miguel Andujar (X - X - X)
inn.new_ab()
inn.pitch_list("c")
inn.out("G5-3")


# Bot 8th
# Pitching: NYY #48 Tommy Kahnle
inn = game.new_inning()

# Pitching change (NYY): #48 Tommy Kahnle replaces #30 David Robertson
inn.pitching_substitution(48)

# 5. BOS #18 Mitch Moreland (X - X - X)
inn.new_ab()
inn.pitch_list("b f c s")
inn.out("K")

# 6. BOS #36 Eduardo Núñez (X - X - X)
inn.new_ab()
inn.pitch_list("b c")
inn.out("G5-3")

# 7. BOS #12 Brock Holt (X - X - X)
inn.new_ab()
inn.pitch_list("c s f b b")
inn.out("L8")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #22 Rick Porcello
inn = game.new_inning()

# 8. NYY #28 Austin Romine (X - X - X)
inn.new_ab()
inn.pitch_list("c")
inn.out("L8")

# 9. NYY #14 Neil Walker (X - X - X)
inn.new_ab()
inn.out("F8")

# 1. NYY #11 Brett Gardner (X - X - X)
inn.new_ab()
inn.pitch_list("c c f b")
inn.out("G6-3")

# Winning team: BOS
# WP: BOS #22 Rick Porcello
game.winning_pitcher(22)

# Loser team: NYY
# LP: NYY #40 Luis Severino
game.losing_pitcher(40, is_away_team=True)

#print(game)
game.generate_scorecard()
