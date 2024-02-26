#TODO решить
SELECT Submissions.parent_id AS post_id, COUNT(Submissions.parent_id) AS number_of_comments
FROM Submissions
GROUP BY parent_id
ORDER BY post_id DESC;

SELECT S1.sub_id, COUNT(S2.parent_id) AS number_of_comments
FROM Submissions AS S1 INNER JOIN Submissions AS S2 ON S1.sub_id = S2.parent_id
WHERE S1.parent_id IS NULL
GROUP BY S1.sub_id;

SELECT sub_id, (SELECT parent_id FROM Submissions AS S2 WHERE S1.sub_id IN (S2.parent_id))
FROM Submissions AS S1
WHERE parent_id IS NULL
GROUP BY sub_id;

SELECT parent_id FROM Submissions AS S2 WHERE 6 IN (parent_id)