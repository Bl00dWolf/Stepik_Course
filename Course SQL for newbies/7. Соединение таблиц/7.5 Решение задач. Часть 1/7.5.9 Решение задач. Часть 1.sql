SELECT Candidates.name, Candidates.surname, COUNT(Votes.id) AS votes_count
FROM Candidates
         INNER JOIN Votes ON Candidates.id = Votes.candidate_id
GROUP BY Candidates.name, Candidates.surname
ORDER BY votes_count DESC
LIMIT 1;