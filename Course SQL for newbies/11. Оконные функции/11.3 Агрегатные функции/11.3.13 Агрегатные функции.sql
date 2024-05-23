SELECT title,
       rating,
       ROUND((SUM(rating) OVER () - rating) / (COUNT(*) OVER () - 1)) as other_films_avg_rating
FROM Films