SELECT extra    AS report_reason,
       COUNT(*) AS report_count
FROM Actions
WHERE action = 'report'
  AND action_date = '2023-07-05'
GROUP BY extra;