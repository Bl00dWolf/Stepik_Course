SELECT title,
       director,
       COUNT(*) OVER () - COUNT(release_year) OVER () -
       IF(release_year IS NULL, 1, 0) as other_films_without_release_year
FROM Films;

# Еще решение
# SELECT title, director,
#        SUM(release_year IS NULL) OVER () - (release_year IS NULL) AS other_films_without_release_year
# FROM Films;
