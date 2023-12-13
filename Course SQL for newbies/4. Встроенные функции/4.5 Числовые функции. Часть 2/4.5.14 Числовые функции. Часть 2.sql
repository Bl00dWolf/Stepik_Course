SELECT title,
       ROUND((flickmetrix + metacritic + imdb + letterboxd + kinopoisk -
              LEAST(flickmetrix, metacritic, imdb, letterboxd, kinopoisk) -
              GREATEST(flickmetrix, metacritic, imdb, letterboxd, kinopoisk)) / 3, 2) as average_rating
FROM Movies
ORDER BY 2 DESC, title;