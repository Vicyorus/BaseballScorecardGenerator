

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


    % bullpen info
    %% bullpen #1
    set_bullpen_name_vars(1);
    label(btex {\bigsf 10} etex, bullpen_no) withcolor clr;
    label(btex {\bigsf John Doe} etex, bullpen_name) withcolor clr;
    label(btex {\bigsf R} etex, bullpen_extra) withcolor clr;

    % batter stats
    %% batter 1-1
    set_batter_total_vars(1, 1, innings);
    label(btex {\bigsf 0} etex, batter_ab) withcolor clr;
    label(btex {\bigsf 0} etex, batter_r) withcolor clr;
    label(btex {\bigsf 0} etex, batter_h) withcolor clr;
    label(btex {\bigsf 0} etex, batter_rbi) withcolor clr;
    label(btex {\bigsf 0} etex, batter_bb) withcolor clr;
    label(btex {\bigsf 0} etex, batter_so) withcolor clr;

    %% batter 2-1
    set_batter_total_vars(2, 1, innings);
    label(btex {\bigsf 0} etex, batter_ab) withcolor clr;
    label(btex {\bigsf 0} etex, batter_r) withcolor clr;
    label(btex {\bigsf 0} etex, batter_h) withcolor clr;
    label(btex {\bigsf 0} etex, batter_rbi) withcolor clr;
    label(btex {\bigsf 0} etex, batter_bb) withcolor clr;
    label(btex {\bigsf 0} etex, batter_so) withcolor clr;

    %% batter 3-1
    set_batter_total_vars(3, 1, innings);
    label(btex {\bigsf 0} etex, batter_ab) withcolor clr;
    label(btex {\bigsf 0} etex, batter_r) withcolor clr;
    label(btex {\bigsf 0} etex, batter_h) withcolor clr;
    label(btex {\bigsf 0} etex, batter_rbi) withcolor clr;
    label(btex {\bigsf 0} etex, batter_bb) withcolor clr;
    label(btex {\bigsf 0} etex, batter_so) withcolor clr;

    %% batter 4-1
    set_batter_total_vars(4, 1, innings);
    label(btex {\bigsf 0} etex, batter_ab) withcolor clr;
    label(btex {\bigsf 0} etex, batter_r) withcolor clr;
    label(btex {\bigsf 0} etex, batter_h) withcolor clr;
    label(btex {\bigsf 0} etex, batter_rbi) withcolor clr;
    label(btex {\bigsf 0} etex, batter_bb) withcolor clr;
    label(btex {\bigsf 0} etex, batter_so) withcolor clr;

    %% batter 5-1
    set_batter_total_vars(5, 1, innings);
    label(btex {\bigsf 0} etex, batter_ab) withcolor clr;
    label(btex {\bigsf 0} etex, batter_r) withcolor clr;
    label(btex {\bigsf 0} etex, batter_h) withcolor clr;
    label(btex {\bigsf 0} etex, batter_rbi) withcolor clr;
    label(btex {\bigsf 0} etex, batter_bb) withcolor clr;
    label(btex {\bigsf 0} etex, batter_so) withcolor clr;

    %% batter 6-1
    set_batter_total_vars(6, 1, innings);
    label(btex {\bigsf 0} etex, batter_ab) withcolor clr;
    label(btex {\bigsf 0} etex, batter_r) withcolor clr;
    label(btex {\bigsf 0} etex, batter_h) withcolor clr;
    label(btex {\bigsf 0} etex, batter_rbi) withcolor clr;
    label(btex {\bigsf 0} etex, batter_bb) withcolor clr;
    label(btex {\bigsf 0} etex, batter_so) withcolor clr;

    %% batter 7-1
    set_batter_total_vars(7, 1, innings);
    label(btex {\bigsf 0} etex, batter_ab) withcolor clr;
    label(btex {\bigsf 0} etex, batter_r) withcolor clr;
    label(btex {\bigsf 0} etex, batter_h) withcolor clr;
    label(btex {\bigsf 0} etex, batter_rbi) withcolor clr;
    label(btex {\bigsf 0} etex, batter_bb) withcolor clr;
    label(btex {\bigsf 0} etex, batter_so) withcolor clr;

    %% batter 8-1
    set_batter_total_vars(8, 1, innings);
    label(btex {\bigsf 0} etex, batter_ab) withcolor clr;
    label(btex {\bigsf 0} etex, batter_r) withcolor clr;
    label(btex {\bigsf 0} etex, batter_h) withcolor clr;
    label(btex {\bigsf 0} etex, batter_rbi) withcolor clr;
    label(btex {\bigsf 0} etex, batter_bb) withcolor clr;
    label(btex {\bigsf 0} etex, batter_so) withcolor clr;

    %% batter 9-1
    set_batter_total_vars(9, 1, innings);
    label(btex {\bigsf 0} etex, batter_ab) withcolor clr;
    label(btex {\bigsf 0} etex, batter_r) withcolor clr;
    label(btex {\bigsf 0} etex, batter_h) withcolor clr;
    label(btex {\bigsf 0} etex, batter_rbi) withcolor clr;
    label(btex {\bigsf 0} etex, batter_bb) withcolor clr;
    label(btex {\bigsf 0} etex, batter_so) withcolor clr;

    %% batter 10-1
    set_batter_total_vars(10, 1, innings);
    label(btex {\bigsf 0} etex, batter_ab) withcolor clr;
    label(btex {\bigsf 0} etex, batter_r) withcolor clr;
    label(btex {\bigsf 0} etex, batter_h) withcolor clr;
    label(btex {\bigsf 0} etex, batter_rbi) withcolor clr;
    label(btex {\bigsf 0} etex, batter_bb) withcolor clr;
    label(btex {\bigsf 0} etex, batter_so) withcolor clr;

    % pitcher stats
    set_pitcher_total_vars(1);
    label(btex {\bigsf 0} etex, pitcher_bf) withcolor clr;
    label(btex {\bigsf 0.0} etex, pitcher_ip) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_h) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_r) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_er) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_bb) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_so) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_ibb) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_hbp) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_blk) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_wp) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_hr) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_pit) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_str) withcolor clr;

    set_pitcher_total_vars(13);
    label(btex {\bigsf 0} etex, pitcher_bf) withcolor clr;
    label(btex {\bigsf 0.0} etex, pitcher_ip) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_h) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_r) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_er) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_bb) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_so) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_ibb) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_hbp) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_blk) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_wp) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_hr) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_pit) withcolor clr;
    label(btex {\bigsf 0} etex, pitcher_str) withcolor clr;


    %% game totals
    set_game_total_vars(innings);
    label(btex {\bigsf 0} etex, inn_run) withcolor clr;
    label(btex {\bigsf 0} etex, inn_hit) withcolor clr;
    label(btex {\bigsf 0} etex, inn_err) withcolor clr;
    label(btex {\bigsf 0} etex, inn_lob) withcolor clr;
    label(btex {\bigsf 0} etex, inn_bb) withcolor clr;
    label(btex {\bigsf 0} etex, inn_so) withcolor clr;
    label(btex {\bigsf 0} etex, inn_pit) withcolor clr;
    label(btex {\bigsf 0} etex, inn_str) withcolor clr;

    %% basepaths totals
    set_basepath_total_vars(innings);
    label.urt(btex {\sf 0} etex, basepath_first_label) withcolor clr;
    label.urt(btex {\sf 0} etex, basepath_second_label) withcolor clr;
    label.urt(btex {\sf 0} etex, basepath_third_label) withcolor clr;
    label.urt(btex {\sf 0} etex, basepath_hr_label) withcolor clr;
    label.urt(btex {\sf 0} etex, basepath_sf_label) withcolor clr;
    label.urt(btex {\sf 0} etex, basepath_sac_label) withcolor clr;

    label.urt(btex {\sf 0} etex, basepath_tb_label) withcolor clr;
    label.urt(btex {\sf 0} etex, basepath_hbp_label) withcolor clr;
    label.urt(btex {\sf 0} etex, basepath_ibb_label) withcolor clr;
    label.urt(btex {\sf 0} etex, basepath_blk_label) withcolor clr;
    label.urt(btex {\sf 0} etex, basepath_wp_label) withcolor clr;
    label.urt(btex {\sf 0} etex, basepath_pb_label) withcolor clr;

    label.urt(btex {\sf 0} etex, basepath_sb_label) withcolor clr;
    label.urt(btex {\sf 0} etex, basepath_cs_label) withcolor clr;
    label.urt(btex {\sf 0} etex, basepath_po_label) withcolor clr;
    label.urt(btex {\sf 0} etex, basepath_dp_label) withcolor clr;
    label.urt(btex {\sf 0} etex, basepath_tp_label) withcolor clr;
    label.urt(btex {\sf 0} etex, basepath_e_label) withcolor clr;

    label.urt(btex {\sf 0+0+0+0+0~~=~~0} etex, basepath_totals_label) withcolor clr;
    label.urt(btex {\sf 0+0+0~~=~~0} etex, basepath_run_lob_opo_label) withcolor clr;
endfig;
end
