SELECT title
FROM Films
WHERE running_time > (SELECT MIN(running_time) FROM Films WHERE director = 'Brad Bird')
ORDER BY title