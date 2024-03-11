SELECT group_id
FROM Students
WHERE group_id NOT IN ((SELECT group_id
                        FROM Students
                        GROUP BY group_id
                        ORDER BY COUNT(*) DESC
                        LIMIT 1),
                       (SELECT group_id
                        FROM Students
                        GROUP BY group_id
                        ORDER BY COUNT(*) ASC
                        LIMIT 1))
GROUP BY group_id;

# Еще вариант
CREATE VIEW StudentsCount (count) AS
SELECT COUNT(name)
FROM Students
GROUP BY group_id;


SELECT group_id
FROM Students
GROUP BY group_id
HAVING COUNT(name) != (SELECT MAX(count) FROM StudentsCount)
   AND COUNT(name) != (SELECT MIN(count) FROM StudentsCount)