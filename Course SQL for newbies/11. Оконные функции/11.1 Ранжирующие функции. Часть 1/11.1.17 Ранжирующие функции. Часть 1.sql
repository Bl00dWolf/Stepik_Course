SELECT ROW_NUMBER() over (PARTITION BY director ORDER BY release_year) as num,
       title,
       director,
       release_year
FROM Films
ORDER BY director, num DESC;