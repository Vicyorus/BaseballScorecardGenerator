EXPECTED_STR_RESULT = """Game info
Date: 1970-01-01 10:00-13:00
At: Testname Park, Cityville
Attendance: 45,000
Weather: 78F, Sunny, 10mph, Out To RF
Scorer: Sco Rer

Away team: Foo Bars

P #1 John Doe (1) 4 AB 2 SO
C #2 John Doe (1) 5 AB 2 R 2 H 1 RBI 2 SO
1B #3 John Doe (1) 4 AB 2 R 2 H 1 RBI 1 SO
2B #4 John Doe (1) 2 AB 1 H 1 RBI 1 SO
    2B #11 John Doe (6) 1 AB 1 R 1 H
3B #5 John Doe (1) 3 AB 1 R 1 H 1 BB 1 SO
SS #6 John Doe (1) 4 AB 2 R 1 H 2 RBI
LF #7 John Doe (1) 4 AB 1 H 1 RBI 2 SO
CF #8 John Doe (1) 4 AB 1 H 2 SO
RF #9 John Doe (1) 3 AB 2 H 1 BB 1 SO

#1 John Doe (1) L 5.0 IP 29 BF 13 H 12 R 11 ER 6 SO 1 WP 2 HR 117 P 79 S
#10 John Doe (6) 3.0 IP 12 BF 2 H 2 R 2 ER 1 BB 3 SO 1 HR 44 P 27 S

~~#11 John Doe (1B)~~
#12 John Doe (CF)
#13 John Doe (C)

~~#10 John Doe (P)~~

R: 8
1B: 8
2B: 2
3B: 0
HR: 2
SAC: 2
SF: 1
DP: 1
TP: 1
SB: 0
CS: 0
PO: 0
PB: 0
E: 2
LOB: 4
RISP: 2-4


Home team: Bar Foos

P #21 Jack Doe (1) 4 AB 2 R 1 H 2 SO
C #22 Jack Doe (1) 5 AB 2 R 2 H 2 RBI 2 SO
1B #23 Jack Doe (1) 5 AB 2 R 3 H 4 RBI
2B #24 Jack Doe (1) 3 AB 1 R 1 H
    PH/2B #31 Jack Doe (6) 1 AB 1 R 1 H 2 RBI 1 BB
3B #25 Jack Doe (1) 5 AB 1 R 1 H 1 RBI 1 SO
SS #26 Jack Doe (1) 4 AB 2 R 2 H 2 RBI 2 SO
LF #27 Jack Doe (1) 4 AB 1 R 2 H 1 RBI 1 SO
CF #28 Jack Doe (1) 4 AB 1 SO
RF #29 Jack Doe (1) 4 AB 2 R 2 H

#21 Jack Doe (1) W 8.0 IP 35 BF 11 H 8 R 8 ER 2 BB 11 SO 1 BLK 1 WP 2 HR 145 P 92 S
#30 Jack Doe (9) S 1.0 IP 4 BF 1 H 1 SO 7 P 7 S

~~#31 Jack Doe (2B)~~
#32 Jack Doe (RF)
#33 Jack Doe (C)

~~#30 Jack Doe (P)~~

R: 14
1B: 5
2B: 7
3B: 0
HR: 3
SAC: 0
SF: 1
DP: 0
TP: 0
SB: 2
CS: 1
PO: 0
PB: 1
E: 2
LOB: 3
RISP: 7-9


Umpires:
HP: HP Umpire
1B: 1B Umpire
2B: 2B Umpire
3B: 3B Umpire
LF: N/A
RF: N/A

Play ball!

Top of the 1st
1. #1 John Doe vs #21 Jack Doe
Pitches: s X
    Out #1: L9

2. #2 John Doe vs #21 Jack Doe
Pitches: b c b c f c
    Out #2: !K

3. #3 John Doe vs #21 Jack Doe
Pitches: s c b b b s
    Out #3: K

Inning totals: 2 K 14 P 9 S

Bottom of the 1st
1. #21 Jack Doe vs #1 John Doe
Pitches: f f b f s
    Out #1: K

2. #22 Jack Doe vs #1 John Doe
Pitches: c b s b s
    Out #2: K

3. #23 Jack Doe vs #1 John Doe
Pitches: c X
    Out #3: G3-1

Inning totals: 2 K 12 P 9 S

Top of the 2nd
4. #4 John Doe vs #21 Jack Doe
Pitches: b b b c c H
    Advance (0 to 1): Hit on 1
    Advance (1 to 2): Advance on 5 BLK
    Out #1: Thrown out (2 to 3), 6 TP5-4-3

5. #5 John Doe vs #21 Jack Doe
Pitches: c H
    Advance (0 to 1): Hit on 1
    Out #2: Thrown out (1 to 2), 6 TP5-4-3

6. #6 John Doe vs #21 Jack Doe
Pitches: f t b s X
    Out #3: TP5-4-3

Inning totals: 2 H 13 P 9 S

Bottom of the 2nd
4. #24 Jack Doe vs #1 John Doe
Pitches: b s b X
    Out #1: G3-1

5. #25 Jack Doe vs #1 John Doe
Pitches: b t b c b X
    Out #2: L7

6. #26 Jack Doe vs #1 John Doe
Pitches: c s b s
    Out #3: K

Inning totals: 1 K 14 P 8 S

Top of the 3rd
7. #7 John Doe vs #21 Jack Doe
Pitches: c f b s
    Out #1: K

8. #8 John Doe vs #21 Jack Doe
Pitches: c b H
    Advance (0 to 1): Hit on 1
    Advance (1 to 2): Advance on 9 1B

9. #9 John Doe vs #21 Jack Doe
Pitches: b b H
    Advance (0 to 1): Hit on 1
    Out #2: Thrown out (1 to 2), 1 DP5-4-3

1. #1 John Doe vs #21 Jack Doe
Pitches: f X
    Out #3: DP5-4-3

Inning totals: 2 H 1 LOB 1 K 12 P 8 S

Bottom of the 3rd
7. #27 Jack Doe vs #1 John Doe
Pitches: c b f H
    Advance (0 to 1): Hit on 1
    Advance (1 to 2): Advance on 29 1B
    Advance (2 to 3): Advance on 21 FC1-6
    Advance (3 to 4): Advance on 22 WP

8. #28 Jack Doe vs #1 John Doe
Pitches: c b b f c
    Out #1: !K

9. #29 Jack Doe vs #1 John Doe
Pitches: s d s H
    Advance (0 to 1): Hit on 1
    Out #2: Thrown out (1 to 2), 21 FC1-6

1. #21 Jack Doe vs #1 John Doe
Pitches: f b d s f R
    Advance (0 to 1): Reach on FC1-6
    Advance (1 to 2): Advance on 22 SB
    Advance (2 to 3): Advance on 22 WP
    Advance (3 to 4): Advance on 22 1B

2. #22 Jack Doe vs #1 John Doe
Pitches: s s f b b b f f f f f H
    Advance (0 to 1): Hit on 1
    Advance (1 to 4): Advance on 23 HR

3. #23 Jack Doe vs #1 John Doe
Pitches: H
    Advance (0 to 4): Hit on 4

4. #24 Jack Doe vs #1 John Doe
Pitches: c b s H
    Advance (0 to 2): Hit on 2
    Advance (2 to 4): Advance on 25 2B

5. #25 Jack Doe vs #1 John Doe
Pitches: H
    Advance (0 to 2): Hit on 2
    Advance (2 to 4): Advance on 26 2B

6. #26 Jack Doe vs #1 John Doe
Pitches: b s d c b H
    Advance (0 to 2): Hit on 2
    Advance (2 to 3): Advance on 27 PB
    Advance (3 to 4): Advance on 27 2B

7. #27 Jack Doe vs #1 John Doe
Pitches: b H
    Advance (0 to 2): Hit on 2
    Out #3: Thrown out (2 to 3), 28 CS

8. #28 Jack Doe vs #1 John Doe
Pitches: c
    No AB: CS

Inning totals: 7 R 8 H 1 K 46 P 32 S

Top of the 4th
2. #2 John Doe vs #21 Jack Doe
Pitches: c H
    Advance (0 to 2): Hit on 2
    Advance (2 to 3): Advance on 3 SAC1-3
    Advance (3 to 4): Advance on 4 SF7

3. #3 John Doe vs #21 Jack Doe
Pitches: b X
    Out #1: SAC1-3

4. #4 John Doe vs #21 Jack Doe
Pitches: X
    Out #2: SF7

5. #5 John Doe vs #21 Jack Doe
Pitches: c s b s
    Out #3: K

Inning totals: 1 R 1 H 1 K 9 P 7 S

Bottom of the 4th
8. #28 Jack Doe vs #1 John Doe
Pitches: b b c s X
    Out #1: G6-3

9. #29 Jack Doe vs #1 John Doe
Pitches: H
    Advance (0 to 1): Hit on 1
    Advance (1 to 3): Advance on 21 2B
    Advance (3 to 4): Advance on 22 2B

1. #21 Jack Doe vs #1 John Doe
Pitches: f b H
    Advance (0 to 2): Hit on 2
    Advance (2 to 3): Advance on 22 2B
    Advance (3 to 4): Advance on 23 1B

2. #22 Jack Doe vs #1 John Doe
Pitches: b H
    Advance (0 to 2): Hit on 2
    Advance (2 to 4): Advance on 23 1B

3. #23 Jack Doe vs #1 John Doe
Pitches: c b b H
    Advance (0 to 1): Hit on 1

4. #24 Jack Doe vs #1 John Doe
Pitches: b b X
    Out #2: (F)P5

5. #25 Jack Doe vs #1 John Doe
Pitches: c s X
    Out #3: F9

Inning totals: 3 R 4 H 1 LOB 21 P 13 S

Top of the 5th
6. #6 John Doe vs #21 Jack Doe
Pitches: c b f b X
    Out #1: F8

7. #7 John Doe vs #21 Jack Doe
Pitches: f f b b f H
    Advance (0 to 1): Hit on 1

8. #8 John Doe vs #21 Jack Doe
Pitches: c f b b c
    Out #2: !K

9. #9 John Doe vs #21 Jack Doe
Pitches: c b s b b s
    Out #3: K

Inning totals: 1 H 1 LOB 2 K 22 P 13 S

Bottom of the 5th
6. #26 Jack Doe vs #1 John Doe
Pitches: c H
    Advance (0 to 4): Hit on 4

7. #27 Jack Doe vs #1 John Doe
Pitches: b f t f b f c
    Out #1: !K

8. #28 Jack Doe vs #1 John Doe
Pitches: f b X
    Out #2: F8

9. #29 Jack Doe vs #1 John Doe
Pitches: c c R
    Advance (0 to 2): Error on E4
    Advance (2 to 3): Advance on 21 SB
    Advance (3 to U): Advance on 21 SF7

1. #21 Jack Doe vs #1 John Doe
Pitches: f b R
    Advance (0 to 1): Reach on SF7

2. #22 Jack Doe vs #1 John Doe
Pitches: c f b d b s
    Out #3: K

Inning totals: 2 R 1 H 2 E 1 LOB 2 K 24 P 17 S

Top of the 6th
1. #1 John Doe vs #21 Jack Doe
Pitches: c f b s
    Out #1: K

2. #2 John Doe vs #21 Jack Doe
Pitches: b b c H
    Advance (0 to 4): Hit on 4

3. #3 John Doe vs #21 Jack Doe
Pitches: c s b H
    Advance (0 to 4): Hit on 4

4. #4 John Doe vs #21 Jack Doe
Pitches: f b f b s
    Out #2: K

5. #5 John Doe vs #21 Jack Doe
Pitches: f X
    Out #3: L6

Inning totals: 2 R 2 H 2 K 19 P 13 S

Bottom of the 6th
Defensive substitution: #11 John Doe
Pitching substitution: #10 John Doe
3. #23 Jack Doe vs #10 John Doe
Pitches: H
    Advance (0 to 2): Hit on 2
    Advance (2 to 4): Advance on 31 HR

Offensive substitution (Pinch-hitter): #31 Jack Doe
4. #31 Jack Doe vs #10 John Doe
Pitches: b H
    Advance (0 to 4): Hit on 4

5. #25 Jack Doe vs #10 John Doe
Pitches: c f b b f b s
    Out #1: K

6. #26 Jack Doe vs #10 John Doe
Pitches: c c b s
    Out #2: K

7. #27 Jack Doe vs #10 John Doe
Pitches: f c b b f b X
    Out #3: L7

Inning totals: 2 R 2 H 2 K 21 P 13 S

Top of the 7th
6. #6 John Doe vs #21 Jack Doe
Pitches: ab f f R
    Advance (0 to 2): Error on E5
    Advance (2 to 3): Advance on 9 DI
    Advance (3 to 4): Advance on 1 SAC1

7. #7 John Doe vs #21 Jack Doe
Pitches: c f f s
    Out #1: K

8. #8 John Doe vs #21 Jack Doe
Pitches: c b b b s f X
    Out #2: (F)P5

9. #9 John Doe vs #21 Jack Doe
Pitches: d b b c b
    Advance (0 to 1): Walk on BB

1. #1 John Doe vs #21 Jack Doe
Pitches: f f b b R
    Advance (0 to 1): Reach on SAC1
    Out #3: Thrown out (1 to 2), 1-4

Inning totals: 1 R 2 E 1 LOB 1 BB 1 K 25 P 16 S

Bottom of the 7th
8. #28 Jack Doe vs #10 John Doe
Pitches: f b b c X
    Out #1: G3-1

9. #29 Jack Doe vs #10 John Doe
Pitches: s X
    Out #2: (F)P3

1. #21 Jack Doe vs #10 John Doe
Pitches: b c b c b f t
    Out #3: KT

Inning totals: 1 K 14 P 9 S

Top of the 8th
2. #2 John Doe vs #21 Jack Doe
Pitches: f b b s f c
    Out #1: !K

3. #3 John Doe vs #21 Jack Doe
Pitches: s b s b f b H
    Advance (0 to 1): Hit on 1
    Advance (1 to 2): Advance on 11 1B
    Advance (2 to 3): Advance on 5 BB
    Advance (3 to 4): Advance on 6 2B

4. #11 John Doe vs #21 Jack Doe
Pitches: H
    Advance (0 to 1): Hit on 1
    Advance (1 to 2): Advance on 5 BB
    Advance (2 to 4): Advance on 6 2B

5. #5 John Doe vs #21 Jack Doe
Pitches: b d b c b
    Advance (0 to 1): Walk on BB
    Advance (1 to 3): Advance on 6 2B
    Advance (3 to 4): Advance on 7 WP

6. #6 John Doe vs #21 Jack Doe
Pitches: b H
    Advance (0 to 2): Hit on 2
    Advance (2 to 3): Advance on 7 WP
    Advance (3 to 4): Advance on 7 G4-3

7. #7 John Doe vs #21 Jack Doe
Pitches: s s b X
    Out #2: G4-3

8. #8 John Doe vs #21 Jack Doe
Pitches: f b b s b s
    Out #3: K

Inning totals: 4 R 3 H 1 BB 2 K 31 P 17 S

Bottom of the 8th
2. #22 Jack Doe vs #10 John Doe
Pitches: c X
    Out #1: P6

3. #23 Jack Doe vs #10 John Doe
Pitches: X
    Out #2: G4-3

4. #31 Jack Doe vs #10 John Doe
Pitches: c b b b b
    Advance (0 to 1): Walk on BB

5. #25 Jack Doe vs #10 John Doe
Pitches: X
    Out #3: G4-3

Inning totals: 1 LOB 1 BB 9 P 5 S

Top of the 9th
Pitching substitution: #30 Jack Doe
9. #9 John Doe vs #30 Jack Doe
Pitches: H
    Advance (0 to 1): Hit on 1

1. #1 John Doe vs #30 Jack Doe
Pitches: s c c
    Out #1: !K

2. #2 John Doe vs #30 Jack Doe
Pitches: s X
    Out #2: F7

3. #3 John Doe vs #30 Jack Doe
Pitches: X
    Out #3: (F)P5

Inning totals: 1 H 1 LOB 1 K 7 P 7 S

"""
