IN1:

INSERT INTO Cricket.Teams (name, country, coach) VALUES
('Team Alpha', 'Country X', 'Coach A'),
('Team Beta', 'Country Y', 'Coach B'),
('Team Gamma', 'Country Z', 'Coach C'),
('Team Delta', 'Country W', 'Coach D');


IN2:

INSERT INTO Cricket.Players (team_id, name, role, batting_style, bowling_style) VALUES
(1, 'Player One', 'Batsman', 'Right-hand', 'Right-arm offbreak'),
(1, 'Player Two', 'Bowler', 'Left-hand', 'Left-arm fast'),
(2, 'Player Three', 'All-rounder', 'Right-hand', 'Right-arm medium'),
(2, 'Player Four', 'Wicketkeeper', 'Right-hand', ''),
(3, 'Player Five', 'Batsman', 'Left-hand', 'Left-arm offbreak'),
(3, 'Player Six', 'Bowler', 'Right-hand', 'Right-arm fast'),
(4, 'Player Seven', 'All-rounder', 'Left-hand', 'Left-arm medium'),
(4, 'Player Eight', 'Wicketkeeper', 'Right-hand', '');
(4, 'Player Nine', 'Bowler', 'Right-hand', 'Right-arm fast');

IN3:

INSERT INTO Cricket.Matches (team_a_id, team_b_id, match_date, venue, match_type) VALUES
(1, 2, '2024-03-15', 'Stadium X', 'Test'),
(1, 2, '2024-03-22', 'Stadium Y', 'ODI'),
(3, 4, '2024-04-10', 'Stadium C', 'T20'),
(1, 3, '2024-04-18', 'Stadium D', 'ODI'),
(2, 4, '2024-04-25', 'Stadium E', 'Test');



INSERT INTO Cricket.MatchResults (match_id, winning_team_id, match_summary) VALUES
(1, 1, 'Team Alpha won by an innings and 52 runs'),
(2, 2, 'Team Beta won by 4 wickets'),
(3, 4, 'Team Delta won by 5 runs'),
(4, 3, 'Team Gamma won by 7 wickets'),
(5, 2, 'Team Beta won by 150 runs');



INSERT INTO Cricket.PlayerMatchPerformance (
    match_id, player_id, runs_scored, balls_faced, wickets_taken, runs_conceded, catches, run_outs
) VALUES
-- Assuming Match 1: Team Alpha vs Team Beta
(1, 1, 75, 50, 0, 0, 2, 0),
(1, 2, 20, 15, 3, 30, 1, 0),
-- Assuming Match 2: Team Gamma vs Team Delta
(2, 5, 45, 35, 0, 0, 1, 1),
(2, 8, 0, 0, 2, 20, 2, 1),
-- For newly added matches
(3, 3, 30, 25, 0, 0, 0, 0),
(3, 6, 5, 7, 4, 24, 1, 0),
(4, 7, 55, 40, 0, 0, 1, 0),
(4, 9, 10, 20, 5, 28, 0, 1); 