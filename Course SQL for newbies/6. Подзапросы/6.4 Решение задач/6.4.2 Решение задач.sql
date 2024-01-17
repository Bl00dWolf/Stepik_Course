SELECT score, (SELECT COUNT(DISTINCT score)
               FROM Scores
               WHERE score >= S.score) AS gamer_rank
FROM Scores AS S
ORDER BY gamer_rank DESC;

# Еще вариант:
# SELECT score,
#        DENSE_RANK() OVER (ORDER BY score DESC) AS gamer_rank
# FROM Scores
# ORDER BY gamer_rank DESC;