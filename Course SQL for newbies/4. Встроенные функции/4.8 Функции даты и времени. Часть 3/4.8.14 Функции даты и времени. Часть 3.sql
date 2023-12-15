SELECT task,
       executor,
       TIMEDIFF(task_end, task_start) AS time_spent
FROM Tasks
ORDER BY 3
LIMIT 1;