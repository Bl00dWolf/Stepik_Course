SELECT name,
       surname,
       CASE
           WHEN time > '01:00:00' THEN 0
           WHEN time < '00:30:00' THEN 100
           ELSE 100 - MINUTE(TIMEDIFF(time, '00:30:00'))
           END AS score
FROM Results
ORDER BY score DESC, name, surname

# еще вариант
# SELECT name,
#        surname,
#        CASE
#            WHEN TIME_TO_SEC(time) / 60 <= 30 THEN 100
#            WHEN TIME_TO_SEC(time) / 60 > 60 THEN 0
#            ELSE ROUND(GREATEST(100 - (TIME_TO_SEC(time) / 60 - 30), 0))
#            END AS score
# FROM Results
# ORDER BY 3 DESC, 1, 2;