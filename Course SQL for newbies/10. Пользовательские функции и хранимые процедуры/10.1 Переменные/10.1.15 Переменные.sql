SET @num_of_rated_directors := (SELECT COUNT(*)
                                FROM Directors
                                WHERE rating IS NOT NULL);