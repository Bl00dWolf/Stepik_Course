SELECT title
FROM Films
WHERE running_time > (SELECT running_time
                      FROM Films as Fm
                      WHERE TO_DAYS(show_date) = TO_DAYS(Films.show_date) - 1)
ORDER BY title;

# еще вариант
# SELECT title
# FROM Films AS F
# WHERE running_time > (SELECT running_time
#                       FROM Films
#                       WHERE show_date = F.show_date - INTERVAL 1 DAY)
# ORDER BY title