

beginfig(0);
    innings := 15;
    draw_full_scorecard(innings);

    clr:=scoring;

    % game data
    set_game_info_vars(innings);
    label.top(btex {\bigsf 1970-01-01 10:00-13:00} etex rotated 90, game_date) withcolor clr;
    label.top(btex {\bigsf 78F, Sunny} etex rotated 90, game_temp) withcolor clr;
    label.top(btex {\bigsf Testname Park, Cityville} etex rotated 90, game_location) withcolor clr;
    label.top(btex {\bigsf 45,000} etex rotated 90, game_attendance) withcolor clr;
    label.top(btex {\bigsf Sco Rer} etex rotated 90, game_scorer) withcolor clr;
    label.top(btex {\bigsf 10mph, Out To RF} etex rotated 90, game_wind) withcolor clr;

    label.top(btex {\bigsf HP Umpire} etex rotated 90, game_hp_ump) withcolor clr;
    label.top(btex {\bigsf 1B Umpire} etex rotated 90, game_first_ump) withcolor clr;
    label.top(btex {\bigsf 2B Umpire} etex rotated 90, game_second_ump) withcolor clr;
    label.top(btex {\bigsf 3B Umpire} etex rotated 90, game_third_ump) withcolor clr;
    label.top(btex {\bigsf N/A} etex rotated 90, game_lf_ump) withcolor clr;
    label.top(btex {\bigsf N/A} etex rotated 90, game_rf_ump) withcolor clr;
    % team info
    label.top(btex {\bigsf Bar Foos} etex rotated 90, game_team) withcolor clr;

    % lineup info
    %% lineup 1-1
    set_batter_name_vars(1, 1);
    label.urt(btex {\bigsf 21} etex, (number_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf Jack Doe} etex, (name_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf 1} etex, (inn_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf 1} etex, (pos_x,player_y)) withcolor clr;

    %% lineup 2-1
    set_batter_name_vars(2, 1);
    label.urt(btex {\bigsf 22} etex, (number_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf Jack Doe} etex, (name_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf 1} etex, (inn_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf 2} etex, (pos_x,player_y)) withcolor clr;

    %% lineup 3-1
    set_batter_name_vars(3, 1);
    label.urt(btex {\bigsf 23} etex, (number_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf Jack Doe} etex, (name_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf 1} etex, (inn_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf 3} etex, (pos_x,player_y)) withcolor clr;

    %% lineup 4-1
    set_batter_name_vars(4, 1);
    label.urt(btex {\bigsf 24} etex, (number_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf Jack Doe} etex, (name_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf 1} etex, (inn_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf 4} etex, (pos_x,player_y)) withcolor clr;

    %% lineup 4-2
    set_batter_name_vars(4, 2);
    label.urt(btex {\bigsf 31} etex, (number_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf Jack Doe} etex, (name_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf 6} etex, (inn_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf PH/4} etex, (pos_x,player_y)) withcolor clr;

    %% lineup 5-1
    set_batter_name_vars(5, 1);
    label.urt(btex {\bigsf 25} etex, (number_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf Jack Doe} etex, (name_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf 1} etex, (inn_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf 5} etex, (pos_x,player_y)) withcolor clr;

    %% lineup 6-1
    set_batter_name_vars(6, 1);
    label.urt(btex {\bigsf 26} etex, (number_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf Jack Doe} etex, (name_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf 1} etex, (inn_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf 6} etex, (pos_x,player_y)) withcolor clr;

    %% lineup 7-1
    set_batter_name_vars(7, 1);
    label.urt(btex {\bigsf 27} etex, (number_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf Jack Doe} etex, (name_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf 1} etex, (inn_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf 7} etex, (pos_x,player_y)) withcolor clr;

    %% lineup 8-1
    set_batter_name_vars(8, 1);
    label.urt(btex {\bigsf 28} etex, (number_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf Jack Doe} etex, (name_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf 1} etex, (inn_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf 8} etex, (pos_x,player_y)) withcolor clr;

    %% lineup 9-1
    set_batter_name_vars(9, 1);
    label.urt(btex {\bigsf 29} etex, (number_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf Jack Doe} etex, (name_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf 1} etex, (inn_x,player_y)) withcolor clr;
    label.urt(btex {\bigsf 9} etex, (pos_x,player_y)) withcolor clr;


    % bench info
    %% bench #1
    set_bench_name_vars(1);
    label(btex {\bigsf 31} etex, bench_no) withcolor clr;
    label(btex {\bigsf Jack Doe} etex, bench_name) withcolor clr;
    label(btex {\bigsf 2B} etex, bench_extra) withcolor clr;
    strikethrough_bench_name(1, clr);

    %% bench #2
    set_bench_name_vars(2);
    label(btex {\bigsf 32} etex, bench_no) withcolor clr;
    label(btex {\bigsf Jack Doe} etex, bench_name) withcolor clr;
    label(btex {\bigsf RF} etex, bench_extra) withcolor clr;

    %% bench #3
    set_bench_name_vars(3);
    label(btex {\bigsf 33} etex, bench_no) withcolor clr;
    label(btex {\bigsf Jack Doe} etex, bench_name) withcolor clr;
    label(btex {\bigsf C} etex, bench_extra) withcolor clr;

    % pitcher info
    %% pitcher #1
    set_pitcher_name_vars(1);
    label.urt(btex {\bigsf 1} etex, pitcher_no) withcolor clr;
    label.urt(btex {\bigsf John Doe} etex, pitcher_name) withcolor clr;
    label.urt(btex {\bigsf L} etex, pitcher_handedness) withcolor clr;
    label.urt(btex {\bigsf 1} etex, pitcher_inn) withcolor clr;

    %% pitcher #2
    set_pitcher_name_vars(2);
    label.urt(btex {\bigsf 10} etex, pitcher_no) withcolor clr;
    label.urt(btex {\bigsf John Doe} etex, pitcher_name) withcolor clr;
    label.urt(btex {\bigsf R} etex, pitcher_handedness) withcolor clr;
    label.urt(btex {\bigsf 6} etex, pitcher_inn) withcolor clr;


    % bullpen info
    %% bullpen #1
    set_bullpen_name_vars(1);
    label(btex {\bigsf 10} etex, bullpen_no) withcolor clr;
    label(btex {\bigsf John Doe} etex, bullpen_name) withcolor clr;
    label(btex {\bigsf R} etex, bullpen_extra) withcolor clr;
    strikethrough_bullpen_name(1, clr);

    % inning #1
    xstart := 0;
    set_inning_num_label_vars(xstart);
    label(btex {\bigsf 1} etex, top_inn_label) withcolor clr;

    %% inning 1, batter 1
    ystart := 1024;
    set_vars(xstart,ystart);
    % pitches
    label(btex {\tiny X} etex, strikeone) withcolor clr;
    label(btex {\tiny X} etex, striketwo) withcolor clr;
    draw_strike_dot(ballone, clr);
    label(btex {\tiny X} etex, strikethree) withcolor clr;
    draw_strike_dot(strikefour, clr);
    % end pitches
    label(btex {\bigsf K} etex, outlabel) withcolor outclr;
    draw_out_one(xstart,ystart,clr);

    %% inning 1, batter 2
    ystart := 896;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_circle(strikeone, clr);
    draw_strike_dot(ballone, clr);
    draw_strike_dot(striketwo, clr);
    draw_strike_dot(balltwo, clr);
    draw_strike_dot(strikethree, clr);
    % end pitches
    label(btex {\bigsf K} etex, outlabel) withcolor outclr;
    draw_out_two(xstart,ystart,clr);

    %% inning 1, batter 3
    ystart := 768;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_circle(strikeone, clr);
    % end pitches
    label(btex {\bigsf G3-1} etex, outlabel) withcolor outclr;
    draw_out_three(xstart,ystart,clr);

    label(btex {\bigsf 1} etex, bot_inn_label) withcolor clr;
    % inning stats
    set_inning_total_vars(xstart);
    label(btex {\bigsf 0} etex, inn_run) withcolor clr;
    label(btex {\bigsf 0} etex, inn_hit) withcolor clr;
    label(btex {\bigsf 0} etex, inn_err) withcolor clr;
    label(btex {\bigsf 0} etex, inn_lob) withcolor clr;
    label(btex {\bigsf 0} etex, inn_bb) withcolor clr;
    label(btex {\bigsf 2} etex, inn_so) withcolor clr;
    label(btex {\bigsf 12} etex, inn_pit) withcolor clr;
    label(btex {\bigsf 9} etex, inn_str) withcolor clr;

    draw_inning_end(xstart,ystart,innendclr);
    % inning #2
    xstart := 128;
    set_inning_num_label_vars(xstart);
    label(btex {\bigsf 2} etex, top_inn_label) withcolor clr;

    %% inning 2, batter 4
    ystart := 640;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_dot(ballone, clr);
    draw_strike_dot(strikeone, clr);
    draw_strike_dot(balltwo, clr);
    % end pitches
    label(btex {\bigsf G3-1} etex, outlabel) withcolor outclr;
    draw_out_one(xstart,ystart,clr);

    %% inning 2, batter 5
    ystart := 512;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_dot(ballone, clr);
    label(btex {\tiny T} etex, strikeone) withcolor clr;
    draw_strike_dot(balltwo, clr);
    draw_strike_circle(striketwo, clr);
    draw_strike_dot(ballthree, clr);
    % end pitches
    label(btex {\bigsf L7} etex, outlabel) withcolor outclr;
    draw_out_two(xstart,ystart,clr);

    %% inning 2, batter 6
    ystart := 384;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_circle(strikeone, clr);
    draw_strike_dot(striketwo, clr);
    draw_strike_dot(ballone, clr);
    draw_strike_dot(strikethree, clr);
    % end pitches
    label(btex {\bigsf K} etex, outlabel) withcolor outclr;
    draw_out_three(xstart,ystart,clr);

    label(btex {\bigsf 2} etex, bot_inn_label) withcolor clr;
    % inning stats
    set_inning_total_vars(xstart);
    label(btex {\bigsf 0} etex, inn_run) withcolor clr;
    label(btex {\bigsf 0} etex, inn_hit) withcolor clr;
    label(btex {\bigsf 0} etex, inn_err) withcolor clr;
    label(btex {\bigsf 0} etex, inn_lob) withcolor clr;
    label(btex {\bigsf 0} etex, inn_bb) withcolor clr;
    label(btex {\bigsf 1} etex, inn_so) withcolor clr;
    label(btex {\bigsf 14} etex, inn_pit) withcolor clr;
    label(btex {\bigsf 8} etex, inn_str) withcolor clr;

    draw_inning_end(xstart,ystart,innendclr);
    % inning #3
    xstart := 256;
    set_inning_num_label_vars(xstart);
    label(btex {\bigsf 3} etex, top_inn_label) withcolor clr;

    %% inning 3, batter 7
    ystart := 256;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_circle(strikeone, clr);
    draw_strike_dot(ballone, clr);
    label(btex {\tiny X} etex, striketwo) withcolor clr;
    % end pitches
    draw_dot(rundot, clr);
    label(btex {\midsf 1B} etex, playloc) withcolor hit;
    draw(single) withcolor hit;
    label.urt(btex {\sf 1B} etex, waysecond) withcolor clr;
    label.urt(btex {\sf 29} etex, waysecond+(0,10)) withcolor clr;
    draw(firstsecond) withcolor clr;
    label.ulft(btex {\sf FC1-6} etex, waythird) withcolor clr;
    label.ulft(btex {\sf 21} etex, waythird+(0,10)) withcolor clr;
    draw(secondthird) withcolor clr;
    label.lft(btex {\sf 22} etex, wayhome+(-1,-2)) withcolor clr;
    label.llft(btex {\sf WP} etex, wayhome+(-1,-5)) withcolor clr;
    draw(thirdhome) withcolor clr;

    %% inning 3, batter 8
    ystart := 128;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_circle(strikeone, clr);
    draw_strike_dot(ballone, clr);
    draw_strike_dot(balltwo, clr);
    label(btex {\tiny X} etex, striketwo) withcolor clr;
    draw_strike_circle(strikethree, clr);
    % end pitches
    draw_strikeout_looking(outlabel, outclr);
    draw_out_one(xstart,ystart,clr);

    %% inning 3, batter 9
    ystart := 0;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_dot(strikeone, clr);
    draw_strike_dot(ballone, clr);
    draw_strike_dot(striketwo, clr);
    % end pitches
    label(btex {\midsf 1B} etex, playloc) withcolor hit;
    draw(single) withcolor hit;
    draw(cs_second) withcolor outclr;
    label.urt(btex {\sf FC1-6} etex, waysecond) withcolor clr;
    label.urt(btex {\sf 21} etex, waysecond+(0,10)) withcolor clr;
    draw_out_two(xstart,ystart,clr);

    %% inning 3, batter 1
    ystart := 1024;
    set_vars(xstart,ystart);
    % pitches
    label(btex {\tiny X} etex, strikeone) withcolor clr;
    draw_strike_dot(ballone, clr);
    draw_strike_dot(balltwo, clr);
    draw_strike_dot(striketwo, clr);
    label(btex {\tiny X} etex, strikethree) withcolor clr;
    % end pitches
    draw_dot(rundot, clr);
    label.lrt(btex {\sf FC1-6} etex, wayfirst) withcolor clr;
    draw(single) withcolor clr;
    label.urt(btex {\sf SB} etex, waysecond) withcolor clr;
    label.urt(btex {\sf 22} etex, waysecond+(0,10)) withcolor clr;
    draw(firstsecond) withcolor clr;
    label.ulft(btex {\sf WP} etex, waythird) withcolor clr;
    label.ulft(btex {\sf 22} etex, waythird+(0,10)) withcolor clr;
    draw(secondthird) withcolor clr;
    label.lft(btex {\sf 22} etex, wayhome+(-1,-2)) withcolor clr;
    label.llft(btex {\sf 1B} etex, wayhome+(-1,-5)) withcolor clr;
    draw(thirdhome) withcolor clr;

    %% inning 3, batter 2
    ystart := 896;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_dot(strikeone, clr);
    draw_strike_dot(striketwo, clr);
    label(btex {\tiny X} etex, strikethree) withcolor clr;
    draw_strike_dot(ballone, clr);
    draw_strike_dot(balltwo, clr);
    draw_strike_dot(ballthree, clr);
    label(btex {\tiny X} etex, strikefour) withcolor clr;
    label(btex {\tiny X} etex, strikefive) withcolor clr;
    label(btex {\tiny X} etex, strikesix) withcolor clr;
    label(btex {\tiny X} etex, strikeseven) withcolor clr;
    label(btex {\tiny X} etex, strikeeight) withcolor clr;
    % end pitches
    draw_dot(rundot, clr);
    draw_diamond(rbione, clr);
    label(btex {\midsf 1B} etex, playloc) withcolor hit;
    draw(single) withcolor hit;
    label.lft(btex {\sf 23} etex, wayhome+(-1,-2)) withcolor clr;
    label.llft(btex {\sf HR} etex, wayhome+(-1,-5)) withcolor clr;
    draw(firsthome) withcolor clr;

    %% inning 3, batter 3
    ystart := 768;
    set_vars(xstart,ystart);
    draw_dot(rundot, clr);
    draw_diamond(rbione, clr);
    draw_diamond(rbitwo, clr);
    label(btex {\midsf HR} etex, playloc) withcolor homer;
    draw(homerun) withcolor homer;

    %% inning 3, batter 4
    ystart := 640;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_circle(strikeone, clr);
    draw_strike_dot(ballone, clr);
    draw_strike_dot(striketwo, clr);
    % end pitches
    draw_dot(rundot, clr);
    label(btex {\midsf 2B} etex, playloc) withcolor hit;
    draw(double) withcolor hit;
    label.lft(btex {\sf 25} etex, wayhome+(-1,-2)) withcolor clr;
    label.llft(btex {\sf 2B} etex, wayhome+(-1,-5)) withcolor clr;
    draw(secondhome) withcolor clr;

    %% inning 3, batter 5
    ystart := 512;
    set_vars(xstart,ystart);
    draw_dot(rundot, clr);
    draw_diamond(rbione, clr);
    label(btex {\midsf 2B} etex, playloc) withcolor hit;
    draw(double) withcolor hit;
    label.lft(btex {\sf 26} etex, wayhome+(-1,-2)) withcolor clr;
    label.llft(btex {\sf 2B} etex, wayhome+(-1,-5)) withcolor clr;
    draw(secondhome) withcolor clr;

    %% inning 3, batter 6
    ystart := 384;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_dot(ballone, clr);
    draw_strike_dot(strikeone, clr);
    draw_strike_dot(balltwo, clr);
    draw_strike_circle(striketwo, clr);
    draw_strike_dot(ballthree, clr);
    % end pitches
    draw_dot(rundot, clr);
    draw_diamond(rbione, clr);
    label(btex {\midsf 2B} etex, playloc) withcolor hit;
    draw(double) withcolor hit;
    label.ulft(btex {\sf PB} etex, waythird) withcolor clr;
    label.ulft(btex {\sf 27} etex, waythird+(0,10)) withcolor clr;
    draw(secondthird) withcolor clr;
    label.lft(btex {\sf 27} etex, wayhome+(-1,-2)) withcolor clr;
    label.llft(btex {\sf 2B} etex, wayhome+(-1,-5)) withcolor clr;
    draw(thirdhome) withcolor clr;

    xstart := 384;
    set_inning_num_label_vars(xstart);

    %% inning 3, batter 7
    ystart := 256;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_dot(ballone, clr);
    % end pitches
    draw_diamond(rbione, clr);
    label(btex {\midsf 2B} etex, playloc) withcolor hit;
    draw(double) withcolor hit;
    draw(cs_third) withcolor outclr;
    label.ulft(btex {\sf CS} etex, waythird) withcolor clr;
    label.ulft(btex {\sf 28} etex, waythird+(0,10)) withcolor clr;
    draw_out_three(xstart,ystart,clr);

    %% inning 3, batter 8
    ystart := 128;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_circle(strikeone, clr);
    % end pitches
    label(btex {\bigsf CS} etex, outlabel) withcolor clr;

    label(btex {\bigsf 3} etex, bot_inn_label) withcolor clr;
    % inning stats
    set_inning_total_vars(xstart);
    label(btex {\bigsf 7} etex, inn_run) withcolor clr;
    label(btex {\bigsf 8} etex, inn_hit) withcolor clr;
    label(btex {\bigsf 0} etex, inn_err) withcolor clr;
    label(btex {\bigsf 0} etex, inn_lob) withcolor clr;
    label(btex {\bigsf 0} etex, inn_bb) withcolor clr;
    label(btex {\bigsf 1} etex, inn_so) withcolor clr;
    label(btex {\bigsf 46} etex, inn_pit) withcolor clr;
    label(btex {\bigsf 32} etex, inn_str) withcolor clr;

    draw_inning_end(xstart,ystart,innendclr);
    % inning #4
    xstart := 512;
    set_inning_num_label_vars(xstart);
    label(btex {\bigsf 4} etex, top_inn_label) withcolor clr;

    %% inning 4, batter 8
    ystart := 128;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_dot(ballone, clr);
    draw_strike_dot(balltwo, clr);
    draw_strike_circle(strikeone, clr);
    draw_strike_dot(striketwo, clr);
    % end pitches
    label(btex {\bigsf G6-3} etex, outlabel) withcolor outclr;
    draw_out_one(xstart,ystart,clr);

    %% inning 4, batter 9
    ystart := 0;
    set_vars(xstart,ystart);
    draw_dot(rundot, clr);
    label(btex {\midsf 1B} etex, playloc) withcolor hit;
    draw(single) withcolor hit;
    label.ulft(btex {\sf 2B} etex, waythird) withcolor clr;
    label.ulft(btex {\sf 21} etex, waythird+(0,10)) withcolor clr;
    draw(firstthird) withcolor clr;
    label.lft(btex {\sf 22} etex, wayhome+(-1,-2)) withcolor clr;
    label.llft(btex {\sf 2B} etex, wayhome+(-1,-5)) withcolor clr;
    draw(thirdhome) withcolor clr;

    %% inning 4, batter 1
    ystart := 1024;
    set_vars(xstart,ystart);
    % pitches
    label(btex {\tiny X} etex, strikeone) withcolor clr;
    draw_strike_dot(ballone, clr);
    % end pitches
    draw_dot(rundot, clr);
    label(btex {\midsf 2B} etex, playloc) withcolor hit;
    draw(double) withcolor hit;
    label.ulft(btex {\sf 2B} etex, waythird) withcolor clr;
    label.ulft(btex {\sf 22} etex, waythird+(0,10)) withcolor clr;
    draw(secondthird) withcolor clr;
    label.lft(btex {\sf 23} etex, wayhome+(-1,-2)) withcolor clr;
    label.llft(btex {\sf 1B} etex, wayhome+(-1,-5)) withcolor clr;
    draw(thirdhome) withcolor clr;

    %% inning 4, batter 2
    ystart := 896;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_dot(ballone, clr);
    % end pitches
    draw_dot(rundot, clr);
    draw_diamond(rbione, clr);
    label(btex {\midsf 2B} etex, playloc) withcolor hit;
    draw(double) withcolor hit;
    label.lft(btex {\sf 23} etex, wayhome+(-1,-2)) withcolor clr;
    label.llft(btex {\sf 1B} etex, wayhome+(-1,-5)) withcolor clr;
    draw(secondhome) withcolor clr;

    %% inning 4, batter 3
    ystart := 768;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_circle(strikeone, clr);
    draw_strike_dot(ballone, clr);
    draw_strike_dot(balltwo, clr);
    % end pitches
    draw_diamond(rbione, clr);
    draw_diamond(rbitwo, clr);
    label(btex {\midsf 1B} etex, playloc) withcolor hit;
    draw(single) withcolor hit;

    %% inning 4, batter 4
    ystart := 640;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_dot(ballone, clr);
    draw_strike_dot(balltwo, clr);
    % end pitches
    label(btex {\bigsf (F)P5} etex, outlabel) withcolor outclr;
    draw_out_two(xstart,ystart,clr);

    %% inning 4, batter 5
    ystart := 512;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_circle(strikeone, clr);
    draw_strike_dot(striketwo, clr);
    % end pitches
    label(btex {\bigsf F9} etex, outlabel) withcolor outclr;
    draw_out_three(xstart,ystart,clr);

    label(btex {\bigsf 4} etex, bot_inn_label) withcolor clr;
    % inning stats
    set_inning_total_vars(xstart);
    label(btex {\bigsf 3} etex, inn_run) withcolor clr;
    label(btex {\bigsf 4} etex, inn_hit) withcolor clr;
    label(btex {\bigsf 0} etex, inn_err) withcolor clr;
    label(btex {\bigsf 1} etex, inn_lob) withcolor clr;
    label(btex {\bigsf 0} etex, inn_bb) withcolor clr;
    label(btex {\bigsf 0} etex, inn_so) withcolor clr;
    label(btex {\bigsf 21} etex, inn_pit) withcolor clr;
    label(btex {\bigsf 13} etex, inn_str) withcolor clr;

    draw_inning_end(xstart,ystart,innendclr);
    % inning #5
    xstart := 640;
    set_inning_num_label_vars(xstart);
    label(btex {\bigsf 5} etex, top_inn_label) withcolor clr;

    %% inning 5, batter 6
    ystart := 384;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_circle(strikeone, clr);
    % end pitches
    draw_dot(rundot, clr);
    draw_diamond(rbione, clr);
    label(btex {\midsf HR} etex, playloc) withcolor homer;
    draw(homerun) withcolor homer;

    %% inning 5, batter 7
    ystart := 256;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_dot(ballone, clr);
    label(btex {\tiny X} etex, strikeone) withcolor clr;
    label(btex {\tiny T} etex, striketwo) withcolor clr;
    label(btex {\tiny X} etex, strikethree) withcolor clr;
    draw_strike_dot(balltwo, clr);
    label(btex {\tiny X} etex, strikefour) withcolor clr;
    draw_strike_circle(strikefive, clr);
    % end pitches
    draw_strikeout_looking(outlabel, outclr);
    draw_out_one(xstart,ystart,clr);

    %% inning 5, batter 8
    ystart := 128;
    set_vars(xstart,ystart);
    % pitches
    label(btex {\tiny X} etex, strikeone) withcolor clr;
    draw_strike_dot(ballone, clr);
    % end pitches
    label(btex {\bigsf F8} etex, outlabel) withcolor outclr;
    draw_out_two(xstart,ystart,clr);

    %% inning 5, batter 9
    ystart := 0;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_circle(strikeone, clr);
    draw_strike_circle(striketwo, clr);
    % end pitches
    draw_cross(rundot, clr);
    label.urt(btex {\sf E4} etex, waysecond) withcolor clr;
    draw(double) withcolor error;
    label.ulft(btex {\sf SB} etex, waythird) withcolor clr;
    label.ulft(btex {\sf 21} etex, waythird+(0,10)) withcolor clr;
    draw(secondthird) withcolor clr;
    label.lft(btex {\sf 21} etex, wayhome+(-1,-2)) withcolor clr;
    label.llft(btex {\sf SF7} etex, wayhome+(-1,-5)) withcolor clr;
    draw(thirdhome) withcolor clr;

    %% inning 5, batter 1
    ystart := 1024;
    set_vars(xstart,ystart);
    % pitches
    label(btex {\tiny X} etex, strikeone) withcolor clr;
    draw_strike_dot(ballone, clr);
    % end pitches
    label.lrt(btex {\sf SF7} etex, wayfirst) withcolor clr;
    draw(single) withcolor clr;

    %% inning 5, batter 2
    ystart := 896;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_circle(strikeone, clr);
    label(btex {\tiny X} etex, striketwo) withcolor clr;
    draw_strike_dot(ballone, clr);
    draw_strike_dot(balltwo, clr);
    draw_strike_dot(ballthree, clr);
    draw_strike_dot(strikethree, clr);
    % end pitches
    label(btex {\bigsf K} etex, outlabel) withcolor outclr;
    draw_out_three(xstart,ystart,clr);

    label(btex {\bigsf 5} etex, bot_inn_label) withcolor clr;
    % inning stats
    set_inning_total_vars(xstart);
    label(btex {\bigsf 2} etex, inn_run) withcolor clr;
    label(btex {\bigsf 1} etex, inn_hit) withcolor clr;
    label(btex {\bigsf 2} etex, inn_err) withcolor clr;
    label(btex {\bigsf 1} etex, inn_lob) withcolor clr;
    label(btex {\bigsf 0} etex, inn_bb) withcolor clr;
    label(btex {\bigsf 2} etex, inn_so) withcolor clr;
    label(btex {\bigsf 24} etex, inn_pit) withcolor clr;
    label(btex {\bigsf 17} etex, inn_str) withcolor clr;

    draw_inning_end(xstart,ystart,innendclr);
    % inning #6
    xstart := 768;
    set_inning_num_label_vars(xstart);
    label(btex {\bigsf 6} etex, top_inn_label) withcolor clr;

    % pitching substitution
    ystart := 768;
    set_vars(xstart,ystart);
    draw(new_pitcher) withcolor pitcherclr;

    %% inning 6, batter 3
    ystart := 768;
    set_vars(xstart,ystart);
    draw_dot(rundot, clr);
    label(btex {\midsf 2B} etex, playloc) withcolor hit;
    draw(double) withcolor hit;
    label.lft(btex {\sf 31} etex, wayhome+(-1,-2)) withcolor clr;
    label.llft(btex {\sf HR} etex, wayhome+(-1,-5)) withcolor clr;
    draw(secondhome) withcolor clr;

    % offensive substitution: pinch-hitter
    ystart := 640;
    set_vars(xstart,ystart);
    draw(new_hitter) withcolor batterclr;

    %% inning 6, batter 4
    ystart := 640;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_dot(ballone, clr);
    % end pitches
    draw_dot(rundot, clr);
    draw_diamond(rbione, clr);
    draw_diamond(rbitwo, clr);
    label(btex {\midsf HR} etex, playloc) withcolor homer;
    draw(homerun) withcolor homer;

    %% inning 6, batter 5
    ystart := 512;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_circle(strikeone, clr);
    label(btex {\tiny X} etex, striketwo) withcolor clr;
    draw_strike_dot(ballone, clr);
    draw_strike_dot(balltwo, clr);
    label(btex {\tiny X} etex, strikethree) withcolor clr;
    draw_strike_dot(ballthree, clr);
    draw_strike_dot(strikefour, clr);
    % end pitches
    label(btex {\bigsf K} etex, outlabel) withcolor outclr;
    draw_out_one(xstart,ystart,clr);

    %% inning 6, batter 6
    ystart := 384;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_circle(strikeone, clr);
    draw_strike_circle(striketwo, clr);
    draw_strike_dot(ballone, clr);
    draw_strike_dot(strikethree, clr);
    % end pitches
    label(btex {\bigsf K} etex, outlabel) withcolor outclr;
    draw_out_two(xstart,ystart,clr);

    %% inning 6, batter 7
    ystart := 256;
    set_vars(xstart,ystart);
    % pitches
    label(btex {\tiny X} etex, strikeone) withcolor clr;
    draw_strike_circle(striketwo, clr);
    draw_strike_dot(ballone, clr);
    draw_strike_dot(balltwo, clr);
    label(btex {\tiny X} etex, strikethree) withcolor clr;
    draw_strike_dot(ballthree, clr);
    % end pitches
    label(btex {\bigsf L7} etex, outlabel) withcolor outclr;
    draw_out_three(xstart,ystart,clr);

    label(btex {\bigsf 6} etex, bot_inn_label) withcolor clr;
    % inning stats
    set_inning_total_vars(xstart);
    label(btex {\bigsf 2} etex, inn_run) withcolor clr;
    label(btex {\bigsf 2} etex, inn_hit) withcolor clr;
    label(btex {\bigsf 0} etex, inn_err) withcolor clr;
    label(btex {\bigsf 0} etex, inn_lob) withcolor clr;
    label(btex {\bigsf 0} etex, inn_bb) withcolor clr;
    label(btex {\bigsf 2} etex, inn_so) withcolor clr;
    label(btex {\bigsf 21} etex, inn_pit) withcolor clr;
    label(btex {\bigsf 13} etex, inn_str) withcolor clr;

    draw_inning_end(xstart,ystart,innendclr);
    % inning #7
    xstart := 896;
    set_inning_num_label_vars(xstart);
    label(btex {\bigsf 7} etex, top_inn_label) withcolor clr;

    %% inning 7, batter 8
    ystart := 128;
    set_vars(xstart,ystart);
    % pitches
    label(btex {\tiny X} etex, strikeone) withcolor clr;
    draw_strike_dot(ballone, clr);
    draw_strike_dot(balltwo, clr);
    draw_strike_circle(striketwo, clr);
    % end pitches
    label(btex {\bigsf G3-1} etex, outlabel) withcolor outclr;
    draw_out_one(xstart,ystart,clr);

    %% inning 7, batter 9
    ystart := 0;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_dot(strikeone, clr);
    % end pitches
    label(btex {\bigsf (F)P3} etex, outlabel) withcolor outclr;
    draw_out_two(xstart,ystart,clr);

    %% inning 7, batter 1
    ystart := 1024;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_dot(ballone, clr);
    draw_strike_circle(strikeone, clr);
    draw_strike_dot(balltwo, clr);
    draw_strike_circle(striketwo, clr);
    draw_strike_dot(ballthree, clr);
    label(btex {\tiny X} etex, strikethree) withcolor clr;
    label(btex {\tiny T} etex, strikefour) withcolor clr;
    % end pitches
    label(btex {\bigsf KT} etex, outlabel) withcolor outclr;
    draw_out_three(xstart,ystart,clr);

    label(btex {\bigsf 7} etex, bot_inn_label) withcolor clr;
    % inning stats
    set_inning_total_vars(xstart);
    label(btex {\bigsf 0} etex, inn_run) withcolor clr;
    label(btex {\bigsf 0} etex, inn_hit) withcolor clr;
    label(btex {\bigsf 0} etex, inn_err) withcolor clr;
    label(btex {\bigsf 0} etex, inn_lob) withcolor clr;
    label(btex {\bigsf 0} etex, inn_bb) withcolor clr;
    label(btex {\bigsf 1} etex, inn_so) withcolor clr;
    label(btex {\bigsf 14} etex, inn_pit) withcolor clr;
    label(btex {\bigsf 9} etex, inn_str) withcolor clr;

    draw_inning_end(xstart,ystart,innendclr);
    % inning #8
    xstart := 1024;
    set_inning_num_label_vars(xstart);
    label(btex {\bigsf 8} etex, top_inn_label) withcolor clr;

    %% inning 8, batter 2
    ystart := 896;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_circle(strikeone, clr);
    % end pitches
    label(btex {\bigsf P6} etex, outlabel) withcolor outclr;
    draw_out_one(xstart,ystart,clr);

    %% inning 8, batter 3
    ystart := 768;
    set_vars(xstart,ystart);
    label(btex {\bigsf G4-3} etex, outlabel) withcolor outclr;
    draw_out_two(xstart,ystart,clr);

    %% inning 8, batter 4
    ystart := 640;
    set_vars(xstart,ystart);
    % pitches
    draw_strike_circle(strikeone, clr);
    draw_strike_dot(ballone, clr);
    draw_strike_dot(balltwo, clr);
    draw_strike_dot(ballthree, clr);
    draw_strike_dot(ballfour, clr);
    % end pitches
    label(btex {\midsf BB} etex, playloc) withcolor walk;
    draw(single) withcolor walk;

    %% inning 8, batter 5
    ystart := 512;
    set_vars(xstart,ystart);
    label(btex {\bigsf G4-3} etex, outlabel) withcolor outclr;
    draw_out_three(xstart,ystart,clr);

    label(btex {\bigsf 8} etex, bot_inn_label) withcolor clr;
    % inning stats
    set_inning_total_vars(xstart);
    label(btex {\bigsf 0} etex, inn_run) withcolor clr;
    label(btex {\bigsf 0} etex, inn_hit) withcolor clr;
    label(btex {\bigsf 0} etex, inn_err) withcolor clr;
    label(btex {\bigsf 1} etex, inn_lob) withcolor clr;
    label(btex {\bigsf 1} etex, inn_bb) withcolor clr;
    label(btex {\bigsf 0} etex, inn_so) withcolor clr;
    label(btex {\bigsf 9} etex, inn_pit) withcolor clr;
    label(btex {\bigsf 5} etex, inn_str) withcolor clr;

    draw_inning_end(xstart,ystart,innendclr);
    % batter stats
    %% batter 1-1
    set_batter_total_vars(1, 1, innings);
    label(btex {\bigsf 4} etex, batter_ab) withcolor clr;
    label(btex {\bigsf 2} etex, batter_r) withcolor clr;
    label(btex {\bigsf 1} etex, batter_h) withcolor clr;
    label(btex {\bigsf 0} etex, batter_rbi) withcolor clr;
    label(btex {\bigsf 0} etex, batter_bb) withcolor clr;
    label(btex {\bigsf 2} etex, batter_so) withcolor clr;

    %% batter 2-1
    set_batter_total_vars(2, 1, innings);
    label(btex {\bigsf 5} etex, batter_ab) withcolor clr;
    label(btex {\bigsf 2} etex, batter_r) withcolor clr;
    label(btex {\bigsf 2} etex, batter_h) withcolor clr;
    label(btex {\bigsf 2} etex, batter_rbi) withcolor clr;
    label(btex {\bigsf 0} etex, batter_bb) withcolor clr;
    label(btex {\bigsf 2} etex, batter_so) withcolor clr;

    %% batter 3-1
    set_batter_total_vars(3, 1, innings);
    label(btex {\bigsf 5} etex, batter_ab) withcolor clr;
    label(btex {\bigsf 2} etex, batter_r) withcolor clr;
    label(btex {\bigsf 3} etex, batter_h) withcolor clr;
    label(btex {\bigsf 4} etex, batter_rbi) withcolor clr;
    label(btex {\bigsf 0} etex, batter_bb) withcolor clr;
    label(btex {\bigsf 0} etex, batter_so) withcolor clr;

    %% batter 4-1
    set_batter_total_vars(4, 1, innings);
    label(btex {\bigsf 3} etex, batter_ab) withcolor clr;
    label(btex {\bigsf 1} etex, batter_r) withcolor clr;
    label(btex {\bigsf 1} etex, batter_h) withcolor clr;
    label(btex {\bigsf 0} etex, batter_rbi) withcolor clr;
    label(btex {\bigsf 0} etex, batter_bb) withcolor clr;
    label(btex {\bigsf 0} etex, batter_so) withcolor clr;

    %% batter 4-2
    set_batter_total_vars(4, 2, innings);
    label(btex {\bigsf 1} etex, batter_ab) withcolor clr;
    label(btex {\bigsf 1} etex, batter_r) withcolor clr;
    label(btex {\bigsf 1} etex, batter_h) withcolor clr;
    label(btex {\bigsf 2} etex, batter_rbi) withcolor clr;
    label(btex {\bigsf 1} etex, batter_bb) withcolor clr;
    label(btex {\bigsf 0} etex, batter_so) withcolor clr;

    %% batter 5-1
    set_batter_total_vars(5, 1, innings);
    label(btex {\bigsf 5} etex, batter_ab) withcolor clr;
    label(btex {\bigsf 1} etex, batter_r) withcolor clr;
    label(btex {\bigsf 1} etex, batter_h) withcolor clr;
    label(btex {\bigsf 1} etex, batter_rbi) withcolor clr;
    label(btex {\bigsf 0} etex, batter_bb) withcolor clr;
    label(btex {\bigsf 1} etex, batter_so) withcolor clr;

    %% batter 6-1
    set_batter_total_vars(6, 1, innings);
    label(btex {\bigsf 4} etex, batter_ab) withcolor clr;
    label(btex {\bigsf 2} etex, batter_r) withcolor clr;
    label(btex {\bigsf 2} etex, batter_h) withcolor clr;
    label(btex {\bigsf 2} etex, batter_rbi) withcolor clr;
    label(btex {\bigsf 0} etex, batter_bb) withcolor clr;
    label(btex {\bigsf 2} etex, batter_so) withcolor clr;

    %% batter 7-1
    set_batter_total_vars(7, 1, innings);
    label(btex {\bigsf 4} etex, batter_ab) withcolor clr;
    label(btex {\bigsf 1} etex, batter_r) withcolor clr;
    label(btex {\bigsf 2} etex, batter_h) withcolor clr;
    label(btex {\bigsf 1} etex, batter_rbi) withcolor clr;
    label(btex {\bigsf 0} etex, batter_bb) withcolor clr;
    label(btex {\bigsf 1} etex, batter_so) withcolor clr;

    %% batter 8-1
    set_batter_total_vars(8, 1, innings);
    label(btex {\bigsf 4} etex, batter_ab) withcolor clr;
    label(btex {\bigsf 0} etex, batter_r) withcolor clr;
    label(btex {\bigsf 0} etex, batter_h) withcolor clr;
    label(btex {\bigsf 0} etex, batter_rbi) withcolor clr;
    label(btex {\bigsf 0} etex, batter_bb) withcolor clr;
    label(btex {\bigsf 1} etex, batter_so) withcolor clr;

    %% batter 9-1
    set_batter_total_vars(9, 1, innings);
    label(btex {\bigsf 4} etex, batter_ab) withcolor clr;
    label(btex {\bigsf 2} etex, batter_r) withcolor clr;
    label(btex {\bigsf 2} etex, batter_h) withcolor clr;
    label(btex {\bigsf 0} etex, batter_rbi) withcolor clr;
    label(btex {\bigsf 0} etex, batter_bb) withcolor clr;
    label(btex {\bigsf 0} etex, batter_so) withcolor clr;

    %% batter 10-1
    set_batter_total_vars(10, 1, innings);
    label(btex {\bigsf 39} etex, batter_ab) withcolor clr;
    label(btex {\bigsf 14} etex, batter_r) withcolor clr;
    label(btex {\bigsf 15} etex, batter_h) withcolor clr;
    label(btex {\bigsf 12} etex, batter_rbi) withcolor clr;
    label(btex {\bigsf 1} etex, batter_bb) withcolor clr;
    label(btex {\bigsf 9} etex, batter_so) withcolor clr;

    % pitcher stats
    set_pitcher_total_vars(1);
    label(btex {\bigsf L} etex, pitcher_wls) withcolor clr;
    label(btex {\bigsf 29} etex, pitcher_bf) withcolor clr;
    label(btex {\bigsf 5.0} etex, pitcher_ip) withcolor clr;
    label(btex {\bigsf 13} etex, pitcher_h) withcolor clr;
    label(btex {\bigsf 12} etex, pitcher_r) withcolor clr;
    label(btex {\bigsf 11} etex, pitcher_er) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_bb) withcolor clr;
    label(btex {\bigsf 6} etex, pitcher_so) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_ibb) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_hbp) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_blk) withcolor clr;
    label(btex {\bigsf 1} etex, pitcher_wp) withcolor clr;
    label(btex {\bigsf 2} etex, pitcher_hr) withcolor clr;
    label(btex {\bigsf 117} etex, pitcher_pit) withcolor clr;
    label(btex {\bigsf 79} etex, pitcher_str) withcolor clr;

    set_pitcher_total_vars(2);
    label(btex {\bigsf 12} etex, pitcher_bf) withcolor clr;
    label(btex {\bigsf 3.0} etex, pitcher_ip) withcolor clr;
    label(btex {\bigsf 2} etex, pitcher_h) withcolor clr;
    label(btex {\bigsf 2} etex, pitcher_r) withcolor clr;
    label(btex {\bigsf 2} etex, pitcher_er) withcolor clr;
    label(btex {\bigsf 1} etex, pitcher_bb) withcolor clr;
    label(btex {\bigsf 3} etex, pitcher_so) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_ibb) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_hbp) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_blk) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_wp) withcolor clr;
    label(btex {\bigsf 1} etex, pitcher_hr) withcolor clr;
    label(btex {\bigsf 44} etex, pitcher_pit) withcolor clr;
    label(btex {\bigsf 27} etex, pitcher_str) withcolor clr;

    set_pitcher_total_vars(13);
    label(btex {\bigsf 41} etex, pitcher_bf) withcolor clr;
    label(btex {\bigsf 8.0} etex, pitcher_ip) withcolor clr;
    label(btex {\bigsf 15} etex, pitcher_h) withcolor clr;
    label(btex {\bigsf 14} etex, pitcher_r) withcolor clr;
    label(btex {\bigsf 13} etex, pitcher_er) withcolor clr;
    label(btex {\bigsf 1} etex, pitcher_bb) withcolor clr;
    label(btex {\bigsf 9} etex, pitcher_so) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_ibb) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_hbp) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_blk) withcolor clr;
    label(btex {\bigsf 1} etex, pitcher_wp) withcolor clr;
    label(btex {\bigsf 3} etex, pitcher_hr) withcolor clr;
    label(btex {\bigsf 161} etex, pitcher_pit) withcolor clr;
    label(btex {\bigsf 106} etex, pitcher_str) withcolor clr;


    %% game totals
    set_game_total_vars(innings);
    label(btex {\bigsf 14} etex, inn_run) withcolor clr;
    label(btex {\bigsf 15} etex, inn_hit) withcolor clr;
    label(btex {\bigsf 2} etex, inn_err) withcolor clr;
    label(btex {\bigsf 3} etex, inn_lob) withcolor clr;
    label(btex {\bigsf 1} etex, inn_bb) withcolor clr;
    label(btex {\bigsf 9} etex, inn_so) withcolor clr;
    label(btex {\bigsf 161} etex, inn_pit) withcolor clr;
    label(btex {\bigsf 106} etex, inn_str) withcolor clr;

    %% basepaths totals
    set_basepath_total_vars(innings);
    label.urt(btex {\sf 5} etex, basepath_first_label) withcolor clr;
    label.urt(btex {\sf 7} etex, basepath_second_label) withcolor clr;
    label.urt(btex {\sf 0} etex, basepath_third_label) withcolor clr;
    label.urt(btex {\sf 3} etex, basepath_hr_label) withcolor clr;
    label.urt(btex {\sf 1} etex, basepath_sf_label) withcolor clr;
    label.urt(btex {\sf 0} etex, basepath_sac_label) withcolor clr;

    label.urt(btex {\sf 31} etex, basepath_tb_label) withcolor clr;
    label.urt(btex {\sf 0} etex, basepath_hbp_label) withcolor clr;
    label.urt(btex {\sf 0} etex, basepath_ibb_label) withcolor clr;
    label.urt(btex {\sf 0} etex, basepath_blk_label) withcolor clr;
    label.urt(btex {\sf 1} etex, basepath_wp_label) withcolor clr;
    label.urt(btex {\sf 1} etex, basepath_pb_label) withcolor clr;

    label.urt(btex {\sf 2} etex, basepath_sb_label) withcolor clr;
    label.urt(btex {\sf 1} etex, basepath_cs_label) withcolor clr;
    label.urt(btex {\sf 0} etex, basepath_po_label) withcolor clr;
    label.urt(btex {\sf 0} etex, basepath_dp_label) withcolor clr;
    label.urt(btex {\sf 0} etex, basepath_tp_label) withcolor clr;
    label(btex {\sf 7-9} etex, basepath_risp_label) withcolor clr;

    label.urt(btex {\sf 39+1+0+0+1~~=~~41} etex, basepath_totals_label) withcolor clr;
    label.urt(btex {\sf 14+3+24~~=~~41} etex, basepath_run_lob_opo_label) withcolor clr;
endfig;
end
