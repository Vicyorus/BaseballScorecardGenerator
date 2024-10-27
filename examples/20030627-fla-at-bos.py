#!/usr/bin/python3.10
import os
from baseball_scorecard.baseball_scorecard import Scorecard

# FLA @ BOS, 2003-06-27
# https://www.baseball-reference.com/boxes/BOS/BOS200306270.shtml
# https://www.mlb.com/gameday/marlins-vs-red-sox/2003/06/27/15122/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "extended_roster": True,
        "scorer": "Vicyorus",
        "date": "2003-06-27 19:05-23:12",
        "at": "Fenway Park, Boston, MA",
        "att": "34,764",
        "temp": "93F, Sunny",
        "wind": "16mph, L To R",
        "away": {
            "team": "Florida Marlins",
            "starter": 134321,
            "roster": {
                # Lineup
                334393: {"jersey": 9, "name": "Juan Pierre"},
                112116: {"jersey": 1, "name": "Luis Castillo"},
                121358: {"jersey": 7, "name": "Ivan Rodriguez"},
                136780: {"jersey": 19, "name": "Mike Lowell"},
                113845: {"jersey": 43, "name": "Juan Encarnacion"},
                117601: {"jersey": 25, "name": "Derrek Lee"},
                408234: {"jersey": 20, "name": "Miguel Cabrera"},
                136460: {"jersey": 11, "name": "Alex Gonzalez"},
                116075: {"jersey": 14, "name": "Todd Hollandsworth"},
                # Starting pitcher
                134321: {"jersey": 45, "name": "Carl Pavano"},
                # Bench
                133226: {"jersey": 52, "name": "Mike Redmond"},
                119348: {"jersey": 12, "name": "Mike Mordecai"},
                110532: {"jersey": 22, "name": "Brian Banks"},
                114353: {"jersey": 6, "name": "Andy Fox"},
                # Bullpen
                346862: {"jersey": 39, "name": "Blaine Neal"},
                150373: {"jersey": 58, "name": "Michael Tejera"},
                407485: {"jersey": 56, "name": "Kevin Olsen"},
                276368: {"jersey": 44, "name": "Allen Levrault"},
            },
            "lefties": [150373],
            "lineup": [
                [334393, "8"],
                [112116, "4"],
                [121358, "2"],
                [136780, "5"],
                [113845, "9"],
                [117601, "3"],
                [408234, "7"],
                [136460, "6"],
                [116075, "0"],
            ],
            "bench": [
                [133226, "C"],
                [119348, "3B"],
                [110532, "1B"],
                [114353, "SS"],
            ],
            "bullpen": [346862, 150373, 407485, 276368],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 218294,
            "roster": {
                # Lineup
                113028: {"jersey": 18, "name": "Johnny Damon"},
                123842: {"jersey": 12, "name": "Todd Walker"},
                114596: {"jersey": 5, "name": "Nomar Garciaparra"},
                120903: {"jersey": 24, "name": "Manny Ramirez"},
                120074: {"jersey": 34, "name": "David Ortiz"},
                132788: {"jersey": 15, "name": "Kevin Millar"},
                119811: {"jersey": 7, "name": "Trot Nixon"},
                119482: {"jersey": 11, "name": "Bill Mueller"},
                123660: {"jersey": 33, "name": "Jason Varitek"},
                # Starting pitcher
                218294: {"jersey": 51, "name": "Byung-Hyun Kim"},
                # Bench
                408108: {"jersey": 26, "name": "Freddy Sanchez"},
                119182: {"jersey": 28, "name": "Doug Mirabelli"},
                # Bullpen
                150142: {"jersey": 30, "name": "Ryan Rupe"},
                425126: {"jersey": 57, "name": "Jason Shiell"},
                123801: {"jersey": 49, "name": "Tim Wakefield"},
                123348: {"jersey": 50, "name": "Mike Timlin"},
                121955: {"jersey": 17, "name": "Rudy Seanez"},
                150356: {"jersey": 58, "name": "Hector Almonte"},
            },
            "lefties": [],
            "lineup": [
                [113028, "8"],
                [123842, "4"],
                [114596, "6"],
                [120903, "7"],
                [120074, "0"],
                [132788, "3"],
                [119811, "9"],
                [119482, "5"],
                [123660, "2"],
            ],
            "bench": [
                [408108, "2B"],
                [119182, "C"],
            ],
            "bullpen": [150142, 425126, 123801, 123348, 121955, 150356],
        },
        "umpires": {
            "HP": "Mark Carlson",
            "1B": "Rob Drake",
            "2B": "Gerry Davis",
            "3B": "Paul Nauert",
        },
    },
)

##########################################################
# PLAY BALL!
##########################################################


##########################################################
# 1st Inning
##########################################################
# Top 1st
# Pitching: BOS #51 Byung-Hyun Kim
t1 = game.new_inning()

# 1. FLA #9  Juan Pierre (X - X - X)
t1.new_ab()
t1.hit(1)
t1.advance(2, "1 G5-3")
t1.advance(4, "7 1B")

# 2. FLA #1  Luis Castillo (X - X - 9)
t1.new_ab()
t1.pitch_list("p")
t1.out("G5-3")

# 3. FLA #7  Ivan Rodriguez (X - 9 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("2 b f 2 f f f")
t1.hit(1, rbis=1)
t1.thrown_out(1, "19 DP4-3", 3, 218294)

# 4. FLA #19 Mike Lowell (X - X - 7)
t1.new_ab()
t1.pitch_list("b f 1 c")
t1.out("DP4-3")


# Bot 1st
# Pitching: FLA #45 Carl Pavano
b1 = game.new_inning()

# 1. BOS #18 Johnny Damon (X - X - X)
b1.new_ab()
b1.pitch_list("c c b b f")
b1.hit(2)
b1.advance(4, "12 1B")

# 2. BOS #12 Todd Walker (X - 18 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("f b f b b")
b1.hit(1, rbis=1)
b1.advance(3, "5 2B")
b1.advance(4, "24 HR")

# 3. BOS #5  Nomar Garciaparra (X - X - 12)
b1.new_ab()
b1.pitch_list("s")
b1.hit(2)
b1.advance(4, "24 HR")

# 4. BOS #24 Manny Ramirez (12 - 5 - X)
b1.new_ab(is_risp=True)
b1.hit(4, rbis=3)

# 5. BOS #34 David Ortiz (X - X - X)
b1.new_ab()
b1.pitch_list("c b b")
b1.hit(2)
b1.advance(4, "15 1B")

# 6. BOS #15 Kevin Millar (X - 34 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b c")
b1.hit(1, rbis=1)
b1.advance(2, "7 1B")
b1.advance(3, "11 BB")
b1.advance(4, "33 1B")

# Pitching change (FLA): #58 Michael Tejera replaces #45 Carl Pavano
b1.pitching_substitution(150373)

# 7. BOS #7  Trot Nixon (X - X - 15)
b1.new_ab()
b1.hit(1)
b1.advance(2, "11 BB")
b1.advance(4, "33 1B")

# 8. BOS #11 Bill Mueller (X - 15 - 7)
b1.new_ab(is_risp=True)
b1.pitch_list("c c f b f b f b b")
b1.reach("BB")
b1.advance(2, "33 1B")
b1.advance(4, "18 3B")

# 9. BOS #33 Jason Varitek (15 - 7 - 11)
b1.new_ab(is_risp=True)
b1.pitch_list("b b s f")
b1.hit(1, rbis=2)
b1.advance(4, "18 3B")

# 1. BOS #18 Johnny Damon (X - 11 - 33)
b1.new_ab(is_risp=True)
b1.pitch_list("c c b f b f f f")
b1.hit(3, rbis=2)
b1.advance(4, "12 1B")

# 2. BOS #12 Todd Walker (18 - X - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b s b b f f f")
b1.hit(1, rbis=1)
b1.advance(3, "24 1B")
b1.advance(4, "15 SF8")

# Pitching change (FLA): #44 Allen Levrault replaces #58 Michael Tejera
b1.pitching_substitution(276368)

# 3. BOS #5  Nomar Garciaparra (X - X - 12)
b1.new_ab()
b1.pitch_list("b b b c")
b1.out("P2")

# 4. BOS #24 Manny Ramirez (X - X - 12)
b1.new_ab()
b1.hit(1)
b1.advance(2, "34 BB")
b1.advance(3, "7 BB")
b1.advance(4, "11 2B")

# 5. BOS #34 David Ortiz (12 - X - 24)
b1.new_ab(is_risp=True)
b1.pitch_list("b c b b f b")
b1.reach("BB")
b1.advance(2, "7 BB")
b1.advance(4, "11 2B")

# 6. BOS #15 Kevin Millar (12 - 24 - 34)
b1.new_ab(is_risp=True)
b1.pitch_list("c b")
b1.out("SF8", rbis=1)

# 7. BOS #7  Trot Nixon (X - 24 - 34)
b1.new_ab(is_risp=True)
b1.pitch_list("b b b c f f b")
b1.reach("BB")
b1.advance(3, "11 2B")
b1.advance(4, "18 1B")

# 8. BOS #11 Bill Mueller (24 - 34 - 7)
b1.new_ab(is_risp=True)
b1.pitch_list("b f b f b")
b1.hit(2, rbis=2)
b1.advance(3, "18 1B")
b1.thrown_out(4, "18 7-2", 3, 276368)

# 9. BOS #33 Jason Varitek (7 - 11 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b b b c b")
b1.reach("BB")
b1.advance(2, "18 7-2")

# 1. BOS #18 Johnny Damon (7 - 11 - 33)
b1.new_ab(is_risp=True)
b1.pitch_list("c b c")
b1.hit(1, rbis=1)


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #51 Byung-Hyun Kim
t2 = game.new_inning()

# 5. FLA #43 Juan Encarnacion (X - X - X)
t2.new_ab()
t2.pitch_list("b c f b f f f b b")
t2.reach("BB")
t2.advance(2, "11 BB")

# 6. FLA #25 Derrek Lee (X - X - 43)
t2.new_ab()
t2.pitch_list("c")
t2.out("F8")

# 7. FLA #20 Miguel Cabrera (X - X - 43)
t2.new_ab()
t2.pitch_list("c c s")
t2.out("K")

# 8. FLA #11 Alex Gonzalez (X - X - 43)
t2.new_ab()
t2.pitch_list("b s b b s b")
t2.reach("BB")

# 9. FLA #14 Todd Hollandsworth (X - 43 - 11)
t2.new_ab(is_risp=True)
t2.pitch_list("c f b s")
t2.out("K")


# Bot 2nd
# Pitching: FLA #44 Allen Levrault
b2 = game.new_inning()

# 2. BOS #12 Todd Walker (X - X - X)
b2.new_ab()
b2.pitch_list("b b b b")
b2.reach("BB")
b2.advance(4, "34 HR")

# 3. BOS #5  Nomar Garciaparra (X - X - 12)
b2.new_ab()
b2.pitch_list("f f b f")
b2.out("F9")

# 4. BOS #24 Manny Ramirez (X - X - 12)
b2.new_ab()
b2.pitch_list("b c")
b2.out("F8")

# 5. BOS #34 David Ortiz (X - X - 12)
b2.new_ab()
b2.pitch_list("s b b s b")
b2.hit(4, rbis=2)

# 6. BOS #15 Kevin Millar (X - X - X)
b2.new_ab()
b2.pitch_list("s b b b b")
b2.reach("BB")

# 7. BOS #7  Trot Nixon (X - X - 15)
b2.new_ab()
b2.out("P5")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #51 Byung-Hyun Kim
t3 = game.new_inning()

# 1. FLA #9  Juan Pierre (X - X - X)
t3.new_ab()
t3.pitch_list("b b c b c")
t3.out("G6-3")

# 2. FLA #1  Luis Castillo (X - X - X)
t3.new_ab()
t3.pitch_list("b c")
t3.out("G4-3")

# 3. FLA #7  Ivan Rodriguez (X - X - X)
t3.new_ab()
t3.pitch_list("b b")
t3.hit(1)
t3.advance(2, "19 1B")

# 4. FLA #19 Mike Lowell (X - X - 7)
t3.new_ab()
t3.hit(1)

# 5. FLA #43 Juan Encarnacion (X - 7 - 19)
t3.new_ab(is_risp=True)
t3.pitch_list("b c")
t3.out("F8")


# Bot 3rd
# Pitching: FLA #44 Allen Levrault
b3 = game.new_inning()

# Defensive change (FLA): #52 Mike Redmond replaces #7 Ivan Rodriguez (C), playing C, batting 3rd
b3.defensive_substitution(3, 133226, "2")

# Defensive change (FLA): #6 Andy Fox replaces #19 Mike Lowell (3B), playing 3B, batting 4th
b3.defensive_substitution(4, 114353, "5")

# 8. BOS #11 Bill Mueller (X - X - X)
b3.new_ab()
b3.pitch_list("b c b")
b3.hit(4)

# 9. BOS #33 Jason Varitek (X - X - X)
b3.new_ab()
b3.pitch_list("c s f b s")
b3.out("K")

# 1. BOS #18 Johnny Damon (X - X - X)
b3.new_ab()
b3.pitch_list("b c b b f s")
b3.out("K")

# 2. BOS #12 Todd Walker (X - X - X)
b3.new_ab()
b3.pitch_list("b c f b b f")
b3.hit(1)

# 3. BOS #5  Nomar Garciaparra (X - X - 12)
b3.new_ab()
b3.out("P6")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #51 Byung-Hyun Kim
t4 = game.new_inning()

# 6. FLA #25 Derrek Lee (X - X - X)
t4.new_ab()
t4.pitch_list("b b c")
t4.out("G6-3")

# 7. FLA #20 Miguel Cabrera (X - X - X)
t4.new_ab()
t4.pitch_list("b f s f s")
t4.out("K")

# 8. FLA #11 Alex Gonzalez (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.out("G5-3")


# Bot 4th
# Pitching: FLA #56 Kevin Olsen
b4 = game.new_inning()

# Pitching change (FLA): #56 Kevin Olsen replaces #44 Allen Levrault
b4.pitching_substitution(407485)

# Defensive change (FLA): #12 Mike Mordecai replaces #1 Luis Castillo (2B), playing 2B, batting 2nd
b4.defensive_substitution(2, 119348, "4")

# Offensive change (BOS): Pinch-hitter #28 Doug Mirabelli replaces #24 Manny Ramirez, batting 4th
b4.offensive_substitution(4, 119182, "PH")

# 4. BOS #28 Doug Mirabelli (X - X - X)
b4.new_ab()
b4.pitch_list("c c b f f s")
b4.out("K")

# 5. BOS #34 David Ortiz (X - X - X)
b4.new_ab()
b4.pitch_list("b f b")
b4.out("F8")

# 6. BOS #15 Kevin Millar (X - X - X)
b4.new_ab()
b4.hit(2)
b4.advance(3, "7 1B")
b4.advance(4, "11 1B")

# 7. BOS #7  Trot Nixon (X - 15 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b c b")
b4.hit(1)
b4.advance(2, "11 1B")
b4.advance(4, "33 1B")

# 8. BOS #11 Bill Mueller (15 - X - 7)
b4.new_ab(is_risp=True)
b4.pitch_list("b c b")
b4.hit(1, rbis=1)
b4.advance(3, "33 1B")

# 9. BOS #33 Jason Varitek (X - 7 - 11)
b4.new_ab(is_risp=True)
b4.hit(1, rbis=1)

# 1. BOS #18 Johnny Damon (11 - X - 33)
b4.new_ab(is_risp=True)
b4.pitch_list("c c d b")
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #51 Byung-Hyun Kim
t5 = game.new_inning()

# Defensive change (BOS): #26 Freddy Sanchez replaces #5 Nomar Garciaparra (SS), playing SS, batting 3rd
t5.defensive_substitution(3, 408108, "6")

# Defensive switch (BOS): #28 Doug Mirabelli moves to 1B
t5.defensive_switch(119182, "3")

# Defensive switch (BOS): #15 Kevin Millar moves to LF
t5.defensive_switch(132788, "7")

# 9. FLA #14 Todd Hollandsworth (X - X - X)
t5.new_ab()
t5.pitch_list("f")
t5.out("G3")

# 1. FLA #9  Juan Pierre (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.error(3)
t5.reach("E3", end_base=2)
t5.advance("U", "52 1B")

# 2. FLA #12 Mike Mordecai (X - 9 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("f b c b f c")
t5.out("!K")

# 3. FLA #52 Mike Redmond (X - 9 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("c")
t5.hit(1, rbis=1)
t5.advance(2, "6 HBP")
t5.advance("U", "43 2B")

# 4. FLA #6  Andy Fox (X - X - 52)
t5.new_ab()
t5.pitch_list("b s c")
t5.reach("HBP")
t5.advance("U", "43 2B")

# 5. FLA #43 Juan Encarnacion (X - 52 - 6)
t5.new_ab(is_risp=True)
t5.pitch_list("c")
t5.hit(2, rbis=2)
t5.advance("U", "25 1B")

# 6. FLA #25 Derrek Lee (X - 43 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b b")
t5.hit(1, rbis=1)

# 7. FLA #20 Miguel Cabrera (X - X - 25)
t5.new_ab()
t5.out("F9")


# Bot 5th
# Pitching: FLA #56 Kevin Olsen
b5 = game.new_inning()

# 2. BOS #12 Todd Walker (X - X - X)
b5.new_ab()
b5.pitch_list("s c b f f b f f f f f s")
b5.out("K")

# 3. BOS #26 Freddy Sanchez (X - X - X)
b5.new_ab()
b5.pitch_list("b b c s c")
b5.out("!K")

# 4. BOS #28 Doug Mirabelli (X - X - X)
b5.new_ab()
b5.pitch_list("s b f")
b5.hit(2)
b5.advance(4, "34 1B")

# 5. BOS #34 David Ortiz (X - 28 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("s")
b5.hit(1, rbis=1)

# 6. BOS #15 Kevin Millar (X - X - 34)
b5.new_ab()
b5.pitch_list("c")
b5.out("F9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #30 Ryan Rupe
t6 = game.new_inning()

# Pitching change (BOS): #30 Ryan Rupe replaces #51 Byung-Hyun Kim
t6.pitching_substitution(150142)

# 8. FLA #11 Alex Gonzalez (X - X - X)
t6.new_ab()
t6.pitch_list("c f b s")
t6.out("K")

# 9. FLA #14 Todd Hollandsworth (X - X - X)
t6.new_ab()
t6.pitch_list("b f")
t6.out("G4-3")

# 1. FLA #9  Juan Pierre (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("G3-1")


# Bot 6th
# Pitching: FLA #56 Kevin Olsen
b6 = game.new_inning()

# Defensive change (FLA): #22 Brian Banks replaces #43 Juan Encarnacion (RF), playing RF, batting 5th
b6.defensive_substitution(5, 110532, "9")

# 7. BOS #7  Trot Nixon (X - X - X)
b6.new_ab()
b6.pitch_list("c b b f")
b6.hit(1)
b6.thrown_out(2, "33 DP4-6-3", 2, 407485)

# 8. BOS #11 Bill Mueller (X - X - 7)
b6.new_ab()
b6.pitch_list("f b f c")
b6.out("!K")

# 9. BOS #33 Jason Varitek (X - X - 7)
b6.new_ab()
b6.pitch_list("c b c f b f f f f f")
b6.out("DP4-6-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #17 Rudy Seanez
t7 = game.new_inning()

# Pitching change (BOS): #17 Rudy Seanez replaces #30 Ryan Rupe
t7.pitching_substitution(121955)

# 2. FLA #12 Mike Mordecai (X - X - X)
t7.new_ab()
t7.pitch_list("b f b f f")
t7.out("G4-3")

# 3. FLA #52 Mike Redmond (X - X - X)
t7.new_ab()
t7.pitch_list("b b f b f")
t7.hit(1)
t7.advance(2, "6 WP")

# 4. FLA #6  Andy Fox (X - X - 52)
t7.new_ab(is_risp=True)
t7.pitch_list("b f b b f f f f f b")
t7.wp()
t7.reach("BB")

# 5. FLA #22 Brian Banks (X - 52 - 6)
t7.new_ab(is_risp=True)
t7.pitch_list("c f b s")
t7.out("K")

# 6. FLA #25 Derrek Lee (X - 52 - 6)
t7.new_ab(is_risp=True)
t7.pitch_list("f s b b b f")
t7.out("G6-3")


# Bot 7th
# Pitching: FLA #56 Kevin Olsen
b7 = game.new_inning()

# 1. BOS #18 Johnny Damon (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.hit(1)
b7.advance(3, "12 2B")
b7.advance(4, "26 G4-3")

# 2. BOS #12 Todd Walker (X - X - 18)
b7.new_ab()
b7.pitch_list("f d f f")
b7.hit(2)
b7.advance(3, "26 G4-3")
b7.thrown_out(4, "28 DP8-2", 3, 346862)

# Pitching change (FLA): #39 Blaine Neal replaces #56 Kevin Olsen
b7.pitching_substitution(346862)

# 3. BOS #26 Freddy Sanchez (18 - 12 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b f c f f b b")
b7.out("G4-3", rbis=1)

# 4. BOS #28 Doug Mirabelli (12 - X - X)
b7.new_ab(is_risp=True)
b7.out("DP8-2")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #58 Hector Almonte
t8 = game.new_inning()

# Pitching change (BOS): #58 Hector Almonte replaces #17 Rudy Seanez
t8.pitching_substitution(150356)

# 7. FLA #20 Miguel Cabrera (X - X - X)
t8.new_ab()
t8.pitch_list("b b b c f b")
t8.reach("BB")
t8.advance(2, "14 WP")
t8.advance(3, "14 1B")
t8.advance(4, "12 SF8")

# 8. FLA #11 Alex Gonzalez (X - X - 20)
t8.new_ab()
t8.pitch_list("c f b f")
t8.out("L5")

# 9. FLA #14 Todd Hollandsworth (X - X - 20)
t8.new_ab(is_risp=True)
t8.pitch_list("f c f b")
t8.wp()
t8.hit(1)
t8.advance(2, "9 DI")

# 1. FLA #9  Juan Pierre (20 - X - 14)
t8.new_ab(is_risp=True)
t8.pitch_list("c d b b b")
t8.reach("BB")
t8.thrown_out(2, "52 FC5-4", 3, 150356)

# 2. FLA #12 Mike Mordecai (20 - 14 - 9)
t8.new_ab(is_risp=True)
t8.pitch_list("f c b f f b")
t8.out("SF8", rbis=1)

# 3. FLA #52 Mike Redmond (X - 14 - 9)
t8.new_ab(is_risp=True)
t8.pitch_list("b c f b f f")
t8.reach("FC5-4")


# Bot 8th
# Pitching: FLA #39 Blaine Neal
b8 = game.new_inning()

# 5. BOS #34 David Ortiz (X - X - X)
b8.new_ab()
b8.reach("HBP")
b8.advance(2, "15 1B")
b8.advance(3, "7 BB")
b8.advance(4, "11 2B")

# 6. BOS #15 Kevin Millar (X - X - 34)
b8.new_ab()
b8.hit(1)
b8.advance(2, "7 BB")
b8.advance(4, "11 2B")

# 7. BOS #7  Trot Nixon (X - 34 - 15)
b8.new_ab(is_risp=True)
b8.pitch_list("c b f b b b")
b8.reach("BB")
b8.advance(3, "11 2B")
b8.advance(4, "33 SF8")

# 8. BOS #11 Bill Mueller (34 - 15 - 7)
b8.new_ab(is_risp=True)
b8.pitch_list("b b b c f f")
b8.hit(2, rbis=2)
b8.advance(3, "33 SF8")
b8.advance(4, "12 SF7")

# 9. BOS #33 Jason Varitek (7 - 11 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("s f")
b8.out("SF8", rbis=1)

# 1. BOS #18 Johnny Damon (11 - X - X)
b8.new_ab(is_risp=True)
b8.pitch_list("s c b f")
b8.hit(1)

# 2. BOS #12 Todd Walker (11 - X - 18)
b8.new_ab(is_risp=True)
b8.pitch_list("c")
b8.out("SF7", rbis=1)

# 3. BOS #26 Freddy Sanchez (X - X - 18)
b8.new_ab()
b8.pitch_list("c f c")
b8.out("!K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #58 Hector Almonte
t9 = game.new_inning()

# Pitching change (BOS): #57 Jason Shiell replaces #58 Hector Almonte
t9.pitching_substitution(425126)

# 4. FLA #6  Andy Fox (X - X - X)
t9.new_ab()
t9.pitch_list("b b c b f f f b")
t9.reach("BB")
t9.advance(4, "25 HR")

# 5. FLA #22 Brian Banks (X - X - 6)
t9.new_ab()
t9.pitch_list("b f")
t9.out("F7")

# 6. FLA #25 Derrek Lee (X - X - 6)
t9.new_ab()
t9.pitch_list("c b b")
t9.hit(4, rbis=2)

# 7. FLA #20 Miguel Cabrera (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("L4")

# 8. FLA #11 Alex Gonzalez (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("F8")

# Winning team: BOS
# WP: BOS #51 Byung-Hyun Kim
game.winning_pitcher(218294)

# Loser team: FLA
# LP: FLA #45 Carl Pavano
game.losing_pitcher(134321, is_away_team=True)

# print(game)
game.generate_scorecard()
