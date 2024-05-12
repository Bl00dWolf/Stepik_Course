SELECT ROW_NUMBER() over (ORDER BY release_year) as num,
       title,
       director,
       release_year
FROM Films
ORDER BY num DESC;