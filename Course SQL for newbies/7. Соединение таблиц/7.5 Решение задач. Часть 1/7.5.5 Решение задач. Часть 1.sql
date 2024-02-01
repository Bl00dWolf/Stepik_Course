SELECT C1.user_id AS user_id
FROM Confirmations C1
         CROSS JOIN Confirmations C2 ON C1.user_id = C2.user_id
WHERE ABS(TIME_TO_SEC(TIMEDIFF(C2.time_stamp, C1.time_stamp))) <= 24 * 60 * 60
  AND C1.time_stamp != C2.time_stamp
GROUP BY user_id;

# Еще вариант
SELECT DISTINCT C1.user_id
FROM Confirmations AS C1
INNER JOIN Confirmations AS C2 ON C1.user_id = C2.user_id
WHERE C2.time_stamp > C1.time_stamp AND
      C1.time_stamp + INTERVAL 24 HOUR >= C2.time_stamp