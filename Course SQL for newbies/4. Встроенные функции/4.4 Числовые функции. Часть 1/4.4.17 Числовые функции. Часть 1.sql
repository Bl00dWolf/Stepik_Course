SELECT title,
       director,
       CONCAT(LPAD(running_time DIV 60, 2, 0),
              ':',
              LPAD(running_time MOD 60, 2, 0)) as timing
FROM Films
ORDER BY running_time DESC;