SELECT DENSE_RANK() over (PARTITION BY country ORDER BY rating DESC) AS rank_in_country,
       full_name,
       country,
       rating
FROM Directors
ORDER BY country, rank_in_country DESC, id DESC;