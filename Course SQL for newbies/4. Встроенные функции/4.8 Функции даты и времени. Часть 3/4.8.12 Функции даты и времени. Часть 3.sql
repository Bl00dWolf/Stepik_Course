SELECT task,
       executor,
       TIMESTAMPDIFF(DAY, task_start - INTERVAL 1 DAY, task_end) AS days_spent
FROM Tasks
ORDER BY 3 DESC
LIMIT 1;