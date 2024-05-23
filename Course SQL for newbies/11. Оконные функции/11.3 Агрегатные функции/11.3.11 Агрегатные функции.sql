SELECT title,
       director,
       COUNT(*) over (PARTITION BY director) - 1 as films_with_same_director
FROM Films;