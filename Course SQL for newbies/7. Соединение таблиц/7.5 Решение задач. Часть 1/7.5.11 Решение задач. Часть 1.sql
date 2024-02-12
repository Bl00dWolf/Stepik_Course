#TODO решить
SELECT Submissions.parent_id AS post_id, COUNT(Submissions.parent_id) AS number_of_comments
FROM Submissions
GROUP BY parent_id
ORDER BY post_id DESC