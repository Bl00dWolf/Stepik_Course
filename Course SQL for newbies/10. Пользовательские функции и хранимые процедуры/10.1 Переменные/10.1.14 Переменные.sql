SET @avg_usa_rating = (SELECT ROUND(AVG(rating), 2)
                       FROM Directors
                       WHERE country = 'USA');