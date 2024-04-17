
1. ## Cricket.Teams Table:

Description: Stores information about different cricket teams.
Columns:
team_id: A unique identifier for each team, set to auto-increment.
name: The name of the cricket team.
country: The country that the cricket team represents.
coach: The name of the team’s coach.

2. ## Cricket.Players Table:

Description: Contains data about the players, linking them to their respective teams.
Columns:
player_id: A unique identifier for each player, set to auto-increment.
team_id: A reference to the team_id in the Teams table, indicating the team to which the player belongs.
name: The name of the player.
role: The role of the player within the team, such as Batsman or Bowler.
batting_style: The batting style of the player.
bowling_style: The bowling style of the player.
Foreign Key Constraint: The team_id column references the team_id in the Teams table and cascades on delete.

3. ## Cricket.Matches Table:

Description: Maintains records of cricket matches.
Columns:
match_id: A unique identifier for each match, set to auto-increment.
team_a_id: A reference to one of the teams playing the match.
team_b_id: A reference to the other team playing the match.
match_date: The date on which the match is scheduled to be played.
venue: The venue where the match is played.
match_type: The type of match, such as Test, ODI, or T20.
Foreign Key Constraints: Both team_a_id and team_b_id reference the team_id in the Teams table and are set to null on delete.

4. ## Cricket.PlayerMatchPerformance Table:

Description: Records the performance of players in each match.
Columns:
performance_id: A unique identifier for each performance record, set to auto-increment.
match_id: References the match for which the performance is recorded.
player_id: References the player whose performance is recorded.
runs_scored: Runs scored by the player in the match.
balls_faced: Balls faced by the player.
wickets_taken: Wickets taken by the player.
runs_conceded: Runs conceded by the player.
catches: Catches taken by the player.
run_outs: Run-outs made by the player.
Foreign Key Constraints: match_id references match_id in the Matches table and player_id references player_id in the Players table. Both have cascade on delete.

5. ## Cricket.MatchResults Table:

Description: Captures the outcome of cricket matches.
Columns:
result_id: A unique identifier for each match result, set to auto-increment.
match_id: References the match for which the result is being recorded.
winning_team_id: References the team that won the match.
match_summary: A text summary of the match.
Foreign Key Constraints: match_id references match_id in the Matches table and winning_team_id references team_id in the Teams table. The foreign key on match_id cascades on delete.

### General Observation
The AUTO_INCREMENT attribute is used in primary keys to automatically generate unique identifiers for new records.
The SERIAL keyword in the Matches and MatchResults tables is an alias for BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE.
The database maintains referential integrity through the use of foreign keys with cascade delete rules. When a team is deleted, all related players, matches, and match results are also deleted.
The schema allows for the team_a_id and team_b_id in the Matches table to be null, which could represent situations where a team is no longer part of the league or database.
Functional dependencies indicated by comments (FDs) show the relationship between primary keys and other columns in the tables, confirming which columns are functionally determined by the primary keys.
This database schema is well-suited for a cricket management system where teams, players, matches, and match performances are tracked and maintained. It allows for various types of queries involving joins, aggregations, and data management operations pertinent to organizing and analyzing cricket matches.