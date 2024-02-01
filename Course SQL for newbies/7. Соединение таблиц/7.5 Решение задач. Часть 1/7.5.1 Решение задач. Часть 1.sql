SELECT Teams.name AS home_team, TM1.name AS away_team
FROM Teams
         CROSS JOIN Teams AS TM1
WHERE TM1.name != Teams.name;