SELECT question_id
FROM Activity
GROUP BY question_id
ORDER BY SUM(action = 'answer') / SUM(action = 'show') DESC, question_id
LIMIT 1;