#!/usr/bin/python3.10
import os
from baseball_scorecard.baseball_scorecard import Scorecard

# SEA @ BOS, 2024-07-29
# https://www.baseball-reference.com/boxes/BOS/BOS202407290.shtml
# https://www.mlb.com/gameday/mariners-vs-red-sox/2024/07/29/746928/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "extended_roster": True,
        "scorer": "Vicyorus",
        "date": "2024-07-29 19:11-21:58",
        "at": "Fenway Park, Boston, MA",
        "att": "35,007",
        "temp": "72F, Partly Cloudy",
        "wind": "4mph, Out To RF",
        "away": {
            "team": "Seattle Mariners",
            "starter": 669302,
            "roster": {
                # Lineup
                645302: {"jersey": 10, "name": "Victor Robles"},
                668227: {"jersey": 56, "name": "Randy Arozarena"},
                663728: {"jersey": 29, "name": "Cal Raleigh"},
                593871: {"jersey": 7, "name": "Jorge Polanco"},
                670042: {"jersey": 20, "name": "Luke Raley"},
                664238: {"jersey": 25, "name": "Dylan Moore"},
                613564: {"jersey": 35, "name": "Jason Vosler"},
                571745: {"jersey": 17, "name": "Mitch Haniger"},
                668942: {"jersey": 4, "name": "Josh Rojas"},
                # Starting pitcher
                669302: {"jersey": 36, "name": "Logan Gilbert"},
                # Bench
                682988: {"jersey": 27, "name": "Tyler Locklear"},
                641598: {"jersey": 18, "name": "Mitch Garver"},
                687799: {"jersey": 2, "name": "Cade Marlowe"},
                660844: {"jersey": 76, "name": "Leo Rivas"},
                # Bullpen
                676092: {"jersey": 52, "name": "Collin Snider"},
                608723: {"jersey": 30, "name": "Austin Voth"},
                666619: {"jersey": 48, "name": "Gregory Santos"},
                693433: {"jersey": 22, "name": "Bryan Woo"},
                554340: {"jersey": 93, "name": "Yimi García"},
                663423: {"jersey": 46, "name": "Trent Thornton"},
                622491: {"jersey": 58, "name": "Luis Castillo"},
                669923: {"jersey": 68, "name": "George Kirby"},
                662253: {"jersey": 75, "name": "Andrés Muñoz"},
                642048: {"jersey": 60, "name": "Tayler Saucedo"},
                642100: {"jersey": 55, "name": "Gabe Speier"},
                682243: {"jersey": 50, "name": "Bryce Miller"},
            },
            "lefties": [642048, 642100],
            "lineup": [
                [645302, "8"],
                [668227, "7"],
                [663728, "2"],
                [593871, "4"],
                [670042, "9"],
                [664238, "6"],
                [613564, "3"],
                [571745, "0"],
                [668942, "5"],
            ],
            "bench": [
                [682988, "1B"],
                [641598, "DH"],
                [687799, "RF"],
                [660844, "SS"],
            ],
            "bullpen": [
                676092,
                608723,
                666619,
                693433,
                554340,
                663423,
                622491,
                669923,
                662253,
                642048,
                642100,
                682243,
            ],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 601713,
            "roster": {
                # Lineup
                680776: {"jersey": 16, "name": "Jarren Duran"},
                677800: {"jersey": 52, "name": "Wilyer Abreu"},
                807799: {"jersey": 7, "name": "Masataka Yoshida"},
                646240: {"jersey": 11, "name": "Rafael Devers"},
                641933: {"jersey": 17, "name": "Tyler O'Neill"},
                642086: {"jersey": 2, "name": "Dominic Smith"},
                657136: {"jersey": 12, "name": "Connor Wong"},
                666152: {"jersey": 70, "name": "David Hamilton"},
                678882: {"jersey": 43, "name": "Ceddanne Rafaela"},
                # Starting pitcher
                601713: {"jersey": 37, "name": "Nick Pivetta"},
                # Bench
                642197: {"jersey": 73, "name": "Jamie Westbrook"},
                663853: {"jersey": 23, "name": "Romy Gonzalez"},
                608701: {"jersey": 30, "name": "Rob Refsnyder"},
                643376: {"jersey": 28, "name": "Danny Jansen"},
                # Bullpen
                677161: {"jersey": 76, "name": "Zack Kelly"},
                572020: {"jersey": 65, "name": "James Paxton"},
                678394: {"jersey": 66, "name": "Brayan Bello"},
                592155: {"jersey": 71, "name": "Cam Booser"},
                445276: {"jersey": 74, "name": "Kenley Jansen"},
                670174: {"jersey": 25, "name": "Josh Winckowski"},
                657514: {"jersey": 83, "name": "Brennan Bernardino"},
                690544: {"jersey": 78, "name": "Bailey Horn"},
                676710: {"jersey": 50, "name": "Kutter Crawford"},
                622259: {"jersey": 61, "name": "Trey Wingenter"},
                681867: {"jersey": 64, "name": "Cooper Criswell"},
                656557: {"jersey": 89, "name": "Tanner Houck"},
            },
            "lefties": [572020, 592155, 657514, 690544],
            "lineup": [
                [680776, "8"],
                [677800, "9"],
                [807799, "0"],
                [646240, "5"],
                [641933, "7"],
                [642086, "3"],
                [657136, "2"],
                [666152, "4"],
                [678882, "6"],
            ],
            "bench": [
                [642197, "2B"],
                [663853, "1B"],
                [608701, "LF"],
                [643376, "C"],
            ],
            "bullpen": [
                677161,
                572020,
                678394,
                592155,
                445276,
                670174,
                657514,
                690544,
                676710,
                622259,
                681867,
                656557,
            ],
        },
        "umpires": {
            "HP": "Andy Fletcher",
            "1B": "Jansen Visconti",
            "2B": "Cory Blaser",
            "3B": "John Bacon",
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
# Pitching: BOS #37 Nick Pivetta
t1 = game.new_inning()

# 1. SEA #10 Victor Robles (X - X - X)
t1.new_ab()
t1.pitch_list("s")
t1.out("L9")

# 2. SEA #56 Randy Arozarena (X - X - X)
t1.new_ab()
t1.pitch_list("b c b c f c")
t1.out("!K")

# 3. SEA #29 Cal Raleigh (X - X - X)
t1.new_ab()
t1.pitch_list("s c b b b s")
t1.out("K")


# Bot 1st
# Pitching: SEA #36 Logan Gilbert
b1 = game.new_inning()

# 1. BOS #16 Jarren Duran (X - X - X)
b1.new_ab()
b1.pitch_list("f f b f s")
b1.out("K")

# 2. BOS #52 Wilyer Abreu (X - X - X)
b1.new_ab()
b1.pitch_list("c b s b s")
b1.out("K")

# 3. BOS #7  Masataka Yoshida (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("G3-1")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #37 Nick Pivetta
t2 = game.new_inning()

# 4. SEA #7  Jorge Polanco (X - X - X)
t2.new_ab()
t2.pitch_list("b b b c c")
t2.out("F9")

# 5. SEA #20 Luke Raley (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("P6")

# 6. SEA #25 Dylan Moore (X - X - X)
t2.new_ab()
t2.pitch_list("f t b s")
t2.out("K")


# Bot 2nd
# Pitching: SEA #36 Logan Gilbert
b2 = game.new_inning()

# 4. BOS #11 Rafael Devers (X - X - X)
b2.new_ab()
b2.pitch_list("b s b")
b2.out("G3-1")

# 5. BOS #17 Tyler O'Neill (X - X - X)
b2.new_ab()
b2.pitch_list("b t b c b")
b2.out("L7")

# 6. BOS #2  Dominic Smith (X - X - X)
b2.new_ab()
b2.pitch_list("c s b s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #37 Nick Pivetta
t3 = game.new_inning()

# 7. SEA #35 Jason Vosler (X - X - X)
t3.new_ab()
t3.pitch_list("c f b s")
t3.out("K")

# 8. SEA #17 Mitch Haniger (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.hit(1)
t3.advance(2, "4 1B")

# 9. SEA #4  Josh Rojas (X - X - 17)
t3.new_ab()
t3.pitch_list("b b")
t3.hit(1)
t3.thrown_out(2, "10 DP5-4-3", 2, 601713)

# 1. SEA #10 Victor Robles (X - 17 - 4)
t3.new_ab(is_risp=True)
t3.pitch_list("f")
t3.out("DP5-4-3")


# Bot 3rd
# Pitching: SEA #36 Logan Gilbert
b3 = game.new_inning()

# 7. BOS #12 Connor Wong (X - X - X)
b3.new_ab()
b3.pitch_list("c b f")
b3.hit(1)
b3.advance(2, "43 1B")
b3.advance(3, "16 FC1-6")
b3.advance(4, "52 WP")

# 8. BOS #70 David Hamilton (X - X - 12)
b3.new_ab()
b3.pitch_list("c b b f c")
b3.out("!K")

# 9. BOS #43 Ceddanne Rafaela (X - X - 12)
b3.new_ab()
b3.pitch_list("s d s 1")
b3.hit(1)
b3.thrown_out(2, "16 FC1-6", 2, 669302)

# 1. BOS #16 Jarren Duran (X - 12 - 43)
b3.new_ab(is_risp=True)
b3.pitch_list("f b d s f")
b3.reach("FC1-6")
b3.advance(2, "52 SB")
b3.advance(3, "52 WP")
b3.advance(4, "52 1B")

# 2. BOS #52 Wilyer Abreu (12 - X - 16)
b3.new_ab(is_risp=True)
b3.pitch_list("s s f b b b f pso f f f f")
b3.wp()
b3.hit(1, rbis=1)
b3.advance(4, "7 HR")

# 3. BOS #7  Masataka Yoshida (X - X - 52)
b3.new_ab()
b3.hit(4, rbis=2)

# 4. BOS #11 Rafael Devers (X - X - X)
b3.new_ab()
b3.pitch_list("c b s")
b3.hit(2)
b3.advance(4, "17 2B")

# 5. BOS #17 Tyler O'Neill (X - 11 - X)
b3.new_ab(is_risp=True)
b3.hit(2, rbis=1)
b3.advance(4, "2 2B")

# 6. BOS #2  Dominic Smith (X - 17 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("b s d c b")
b3.hit(2, rbis=1)
b3.advance(3, "12 PB")
b3.advance(4, "12 2B")

# Pitching change (SEA): #46 Trent Thornton replaces #36 Logan Gilbert
b3.pitching_substitution(663423)

# 7. BOS #12 Connor Wong (X - 2 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("b")
b3.pb()
b3.hit(2, rbis=1)
b3.thrown_out(3, "70 CS", 3, 663423)

# 8. BOS #70 David Hamilton (X - 12 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("c")
b3.no_ab("CS")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #37 Nick Pivetta
t4 = game.new_inning()

# 2. SEA #56 Randy Arozarena (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.hit(2)
t4.advance(3, "29 G6-3")
t4.advance(4, "7 SF7")

# 3. SEA #29 Cal Raleigh (X - 56 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b")
t4.out("G6-3")

# 4. SEA #7  Jorge Polanco (56 - X - X)
t4.new_ab(is_risp=True)
t4.out("SF7", rbis=1)

# 5. SEA #20 Luke Raley (X - X - X)
t4.new_ab()
t4.pitch_list("c s b s")
t4.out("K")


# Bot 4th
# Pitching: SEA #46 Trent Thornton
b4 = game.new_inning()

# 8. BOS #70 David Hamilton (X - X - X)
b4.new_ab()
b4.pitch_list("b b c s")
b4.out("G6-3")

# 9. BOS #43 Ceddanne Rafaela (X - X - X)
b4.new_ab()
b4.hit(1)
b4.advance(3, "16 2B")
b4.advance(4, "52 2B")

# 1. BOS #16 Jarren Duran (X - X - 43)
b4.new_ab()
b4.pitch_list("1 f b")
b4.hit(2)
b4.advance(3, "52 2B")
b4.advance(4, "7 1B")

# 2. BOS #52 Wilyer Abreu (43 - 16 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b")
b4.hit(2, rbis=1)
b4.advance(4, "7 1B")

# 3. BOS #7  Masataka Yoshida (16 - 52 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("c b b")
b4.hit(1, rbis=2)

# 4. BOS #11 Rafael Devers (X - X - 7)
b4.new_ab()
b4.pitch_list("b b")
b4.out("(F)P5")

# 5. BOS #17 Tyler O'Neill (X - X - 7)
b4.new_ab()
b4.pitch_list("c s")
b4.out("F9")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #37 Nick Pivetta
t5 = game.new_inning()

# 6. SEA #25 Dylan Moore (X - X - X)
t5.new_ab()
t5.pitch_list("c b f b")
t5.out("F8")

# 7. SEA #35 Jason Vosler (X - X - X)
t5.new_ab()
t5.pitch_list("f f b b f")
t5.hit(1)

# 8. SEA #17 Mitch Haniger (X - X - 35)
t5.new_ab()
t5.pitch_list("c f b b c")
t5.out("!K")

# 9. SEA #4  Josh Rojas (X - X - 35)
t5.new_ab()
t5.pitch_list("c b s b b s")
t5.out("K")


# Bot 5th
# Pitching: SEA #46 Trent Thornton
b5 = game.new_inning()

# 6. BOS #2  Dominic Smith (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.hit(4)

# 7. BOS #12 Connor Wong (X - X - X)
b5.new_ab()
b5.pitch_list("b f t f b f c")
b5.out("!K")

# 8. BOS #70 David Hamilton (X - X - X)
b5.new_ab()
b5.pitch_list("f b")
b5.out("F8")

# 9. BOS #43 Ceddanne Rafaela (X - X - X)
b5.new_ab()
b5.pitch_list("c c")
b5.error(4)
b5.reach("E4")
b5.advance("U", "16 2B")

# 1. BOS #16 Jarren Duran (X - X - 43)
b5.new_ab()
b5.pitch_list("f b")
b5.hit(2, rbis=1)

# Pitching change (SEA): #55 Gabe Speier replaces #46 Trent Thornton
b5.pitching_substitution(642100)

# 2. BOS #52 Wilyer Abreu (X - 16 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("c f b d b s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #37 Nick Pivetta
t6 = game.new_inning()

# 1. SEA #10 Victor Robles (X - X - X)
t6.new_ab()
t6.pitch_list("c f b s")
t6.out("K")

# 2. SEA #56 Randy Arozarena (X - X - X)
t6.new_ab()
t6.pitch_list("b b c")
t6.hit(4)

# 3. SEA #29 Cal Raleigh (X - X - X)
t6.new_ab()
t6.pitch_list("c s b")
t6.hit(4)

# 4. SEA #7  Jorge Polanco (X - X - X)
t6.new_ab()
t6.pitch_list("f b f b s")
t6.out("K")

# 5. SEA #20 Luke Raley (X - X - X)
t6.new_ab()
t6.pitch_list("f")
t6.out("L6")


# Bot 6th
# Pitching: SEA #55 Gabe Speier
b6 = game.new_inning()

# Defensive change (SEA): #76 Leo Rivas replaces #7 Jorge Polanco (2B), playing 2B, batting 4th
b6.defensive_substitution(4, 660844, "4")

# 3. BOS #7  Masataka Yoshida (X - X - X)
b6.new_ab()
b6.hit(2)
b6.advance(4, "23 HR")

# Offensive change (BOS): Pinch-hitter #23 Romy Gonzalez replaces #11 Rafael Devers, batting 4th
b6.offensive_substitution(4, 663853, "PH")

# 4. BOS #23 Romy Gonzalez (X - 7 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b")
b6.hit(4, rbis=2)

# 5. BOS #17 Tyler O'Neill (X - X - X)
b6.new_ab()
b6.pitch_list("c f b b f b s")
b6.out("K")

# 6. BOS #2  Dominic Smith (X - X - X)
b6.new_ab()
b6.pitch_list("c c b s")
b6.out("K")

# 7. BOS #12 Connor Wong (X - X - X)
b6.new_ab()
b6.pitch_list("f c b b f b")
b6.out("L7")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #37 Nick Pivetta
t7 = game.new_inning()

# Defensive switch (BOS): #23 Romy Gonzalez moves to 3B
t7.defensive_switch(663853, "5")

# 6. SEA #25 Dylan Moore (X - X - X)
t7.new_ab()
t7.pitch_list("c f b f")
t7.error(5)
t7.reach("E5")
t7.advance(2, "4 DI")
t7.thrown_out(3, "10 FC5", 3, 622259)

# 7. SEA #35 Jason Vosler (X - X - 25)
t7.new_ab()
t7.pitch_list("c f f s")
t7.out("K")

# 8. SEA #17 Mitch Haniger (X - X - 25)
t7.new_ab()
t7.pitch_list("c b b b s f pso")
t7.out("(F)P5")

# 9. SEA #4  Josh Rojas (X - X - 25)
t7.new_ab(is_risp=True)
t7.pitch_list("d b b c b")
t7.reach("BB")

# Pitching change (BOS): #61 Trey Wingenter replaces #37 Nick Pivetta
t7.pitching_substitution(622259)

# 1. SEA #10 Victor Robles (X - 25 - 4)
t7.new_ab(is_risp=True)
t7.pitch_list("f f b b")
t7.reach("FC5")


# Bot 7th
# Pitching: SEA #52 Collin Snider
b7 = game.new_inning()

# Pitching change (SEA): #52 Collin Snider replaces #55 Gabe Speier
b7.pitching_substitution(676092)

# Defensive switch (SEA): #10 Victor Robles moves to LF
b7.defensive_switch(645302, "7")

# Defensive change (SEA): #2 Cade Marlowe replaces #56 Randy Arozarena (LF), playing CF, batting 2nd
b7.defensive_substitution(2, 687799, "8")

# 8. BOS #70 David Hamilton (X - X - X)
b7.new_ab()
b7.pitch_list("f b b c")
b7.out("G3-1")

# 9. BOS #43 Ceddanne Rafaela (X - X - X)
b7.new_ab()
b7.pitch_list("s")
b7.out("(F)P3")

# Offensive change (BOS): Pinch-hitter #73 Jamie Westbrook replaces #16 Jarren Duran, batting 1st
b7.offensive_substitution(1, 642197, "PH")

# 1. BOS #73 Jamie Westbrook (X - X - X)
b7.new_ab()
b7.pitch_list("b c b c b f t")
b7.out("KT")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #61 Trey Wingenter
t8 = game.new_inning()

# Defensive switch (BOS): #73 Jamie Westbrook moves to 2B
t8.defensive_switch(642197, "4")

# Defensive switch (BOS): #70 David Hamilton moves to SS
t8.defensive_switch(666152, "6")

# Defensive switch (BOS): #43 Ceddanne Rafaela moves to CF
t8.defensive_switch(678882, "8")

# 2. SEA #2  Cade Marlowe (X - X - X)
t8.new_ab()
t8.pitch_list("f b b s f c")
t8.out("!K")

# 3. SEA #29 Cal Raleigh (X - X - X)
t8.new_ab()
t8.pitch_list("s b s b f b")
t8.hit(1)
t8.advance(2, "76 1B")
t8.advance(3, "20 BB")
t8.advance(4, "25 2B")

# 4. SEA #76 Leo Rivas (X - X - 29)
t8.new_ab()
t8.hit(1)
t8.advance(2, "20 BB")
t8.advance(4, "25 2B")

# 5. SEA #20 Luke Raley (X - 29 - 76)
t8.new_ab(is_risp=True)
t8.pitch_list("b d b c b")
t8.reach("BB")
t8.advance(3, "25 2B")
t8.advance(4, "35 WP")

# 6. SEA #25 Dylan Moore (29 - 76 - 20)
t8.new_ab(is_risp=True)
t8.pitch_list("b")
t8.hit(2, rbis=2)
t8.advance(3, "35 WP")
t8.advance(4, "35 G4-3")

# 7. SEA #35 Jason Vosler (20 - 25 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("s s b")
t8.wp()
t8.out("G4-3", rbis=1)

# 8. SEA #17 Mitch Haniger (X - X - X)
t8.new_ab()
t8.pitch_list("f b b s b s")
t8.out("K")


# Bot 8th
# Pitching: SEA #60 Tayler Saucedo
b8 = game.new_inning()

# Pitching change (SEA): #60 Tayler Saucedo replaces #52 Collin Snider
b8.pitching_substitution(642048)

# Defensive switch (SEA): #35 Jason Vosler moves to LF
b8.defensive_switch(613564, "7")

# Defensive change (SEA): #27 Tyler Locklear replaces #10 Victor Robles (CF), playing 1B, batting 1st
b8.defensive_substitution(1, 682988, "3")

# 2. BOS #52 Wilyer Abreu (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("P6")

# 3. BOS #7  Masataka Yoshida (X - X - X)
b8.new_ab()
b8.out("G4-3")

# 4. BOS #23 Romy Gonzalez (X - X - X)
b8.new_ab()
b8.pitch_list("c b b b b")
b8.reach("BB")

# 5. BOS #17 Tyler O'Neill (X - X - 23)
b8.new_ab()
b8.out("G4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #78 Bailey Horn
t9 = game.new_inning()

# Pitching change (BOS): #78 Bailey Horn replaces #61 Trey Wingenter
t9.pitching_substitution(690544)

# 9. SEA #4  Josh Rojas (X - X - X)
t9.new_ab()
t9.hit(1)

# 1. SEA #27 Tyler Locklear (X - X - 4)
t9.new_ab()
t9.pitch_list("s c c")
t9.out("!K")

# 2. SEA #2  Cade Marlowe (X - X - 4)
t9.new_ab()
t9.pitch_list("s")
t9.out("F7")

# 3. SEA #29 Cal Raleigh (X - X - 4)
t9.new_ab()
t9.out("(F)P5")

# Winning team: BOS
# WP: BOS #37 Nick Pivetta
game.winning_pitcher(601713)

# Loser team: SEA
# LP: SEA #36 Logan Gilbert
game.losing_pitcher(669302, is_away_team=True)

# print(game)
game.generate_scorecard()
