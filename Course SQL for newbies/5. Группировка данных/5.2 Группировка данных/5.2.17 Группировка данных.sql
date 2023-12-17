SELECT LEFT(name, 1) AS letter,
       COUNT(*)      AS num_of_names
FROM Directors
GROUP BY letter
ORDER BY num_of_names, letter;