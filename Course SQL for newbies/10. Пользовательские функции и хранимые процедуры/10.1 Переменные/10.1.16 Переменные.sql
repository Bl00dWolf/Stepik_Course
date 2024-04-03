SET @min_usa_rating := (SELECT MIN(rating)
                        FROM Directors
                        WHERE country = 'USA');

SELECT @min_usa_rating AS min_usa_rating;