-- SELECT Player
SELECT * FROM Players WHERE team_id = 1;

-- SELECT TEAM

SELECT
        T.name AS team_name,
        T.country,
        P.name AS player_name,
        P.role,
        P.batting_style,
        P.bowling_style
        FROM
        Cricket.Teams AS T
        JOIN
        Cricket.Players AS P ON T.team_id = P.team_id
        where T.team_id = 1;

--ADD Player
INSERT INTO Cricket.Players (team_id, name, role, batting_style, bowling_style) VALUES
(1, 'Player One', 'Batsman', 'Right-hand', 'Right-arm offbreak'),

-- Deleting a player
DELETE FROM Players WHERE name = 'Player Four';
