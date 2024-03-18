WITH VotesCand AS (SELECT candidate, COUNT(voter) as votes
                   FROM Votes
                   GROUP BY candidate
                   ORDER BY votes DESC
                   LIMIT 1)

SELECT candidate
FROM VotesCand;

# Еще вариант
SELECT candidate
FROM Votes
GROUP BY candidate
ORDER BY COUNT(*) DESC
LIMIT 1;
