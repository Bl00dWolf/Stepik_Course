SELECT title, running_time
FROM Films
WHERE running_time < 100
   or running_time > 110
ORDER BY running_time DESC;