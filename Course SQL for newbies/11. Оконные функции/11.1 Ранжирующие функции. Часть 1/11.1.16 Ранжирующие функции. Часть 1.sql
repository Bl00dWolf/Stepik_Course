SELECT ((ROW_NUMBER() over (ORDER BY release_year DESC) - 1) * 5) as num,
       title,
       director,
       release_year
FROM Films
ORDER BY num DESC;