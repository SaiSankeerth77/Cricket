T1:
CREATE TABLE Cricket.Teams (
    team_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each team, auto-incremented
    name VARCHAR(255) NOT NULL,  -- Team name
    country VARCHAR(100) NOT NULL,  -- Country the team represents
    coach VARCHAR(255)  -- Name of the team coach
);

T2:

CREATE TABLE Cricket.Players (
    player_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each player
    team_id INT NOT NULL,  -- The team to which the player belongs
    name VARCHAR(255) NOT NULL,  -- Player's name
    role VARCHAR(100),  -- Player's role (e.g., Batsman, Bowler)
    batting_style VARCHAR(100),  -- Batting style
    bowling_style VARCHAR(100),  -- Bowling style
    FOREIGN KEY (team_id) REFERENCES Cricket.Teams(team_id) ON DELETE CASCADE
);


T3:
-- FDs: player_id → team_id, name, role, batting_style, bowling_style
CREATE TABLE Cricket.Matches (
    match_id SERIAL PRIMARY KEY,  -- Unique identifier for each match
    team_a_id INT,  -- One of the teams playing the match, can be NULL if team is deleted
    team_b_id INT,  -- The other team playing the match, can be NULL if team is deleted
    match_date DATE NOT NULL,  -- Date of the match
    venue VARCHAR(255) NOT NULL,  -- Venue where the match is played
    match_type VARCHAR(50),  -- Type of match (e.g., Test, ODI, T20)
    FOREIGN KEY (team_a_id) REFERENCES Teams(team_id) ON DELETE SET NULL,
    FOREIGN KEY (team_b_id) REFERENCES Teams(team_id) ON DELETE SET NULL
);

T4:
-- FDs: match_id → team_a_id, team_b_id, match_date, venue, match_type
CREATE TABLE Cricket.PlayerMatchPerformance (
    performance_id SERIAL PRIMARY KEY,  -- Unique identifier for each performance record
    match_id BIGINT UNSIGNED NOT NULL,  -- The match for which the performance is recorded, matching the type in Matches
    player_id INT NOT NULL,  -- The player whose performance is recorded
    runs_scored INT,  -- Runs scored by the player in the match
    balls_faced INT,  -- Balls faced by the player
    wickets_taken INT,  -- Wickets taken by the player
    runs_conceded INT,  -- Runs conceded by the player
    catches INT,  -- Catches taken by the player
    run_outs INT,  -- Run-outs made by the player
    FOREIGN KEY (match_id) REFERENCES Matches(match_id) ON DELETE CASCADE,
    FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE
);


T5:

-- FDs: performance_id → match_id, player_id, runs_scored, balls_faced, wickets_taken, runs_conceded, catches, run_outs
CREATE TABLE Cricket.MatchResults (
    result_id SERIAL PRIMARY KEY,  -- Unique identifier for each match result
    match_id BIGINT UNSIGNED NOT NULL,  -- References the match for which the result is recorded, matching the type in Matches
    winning_team_id INT,  -- References the team that won the match
    match_summary TEXT,  -- A text summary of the match
    FOREIGN KEY (match_id) REFERENCES Matches(match_id) ON DELETE CASCADE,
    FOREIGN KEY (winning_team_id) REFERENCES Teams(team_id)
);
