SELECT Suits.suit, Ranks.rankvalue
FROM Suits,
     Ranks
ORDER BY CASE Suits.suit
             WHEN 'Spades' THEN 0
             WHEN 'Clubs' THEN 1
             WHEN 'Diamonds' THEN 2
             WHEN 'Hearts' THEN 3
             END,
         CASE Ranks.rankvalue
             WHEN '2' THEN 0
             WHEN '3' THEN 1
             WHEN '4' THEN 2
             WHEN '5' THEN 3
             WHEN '6' THEN 4
             WHEN '7' THEN 5
             WHEN '8' THEN 6
             WHEN '9' THEN 7
             WHEN '10' THEN 8
             WHEN 'Jack' THEN 9
             WHEN 'Queen' THEN 10
             WHEN 'King' THEN 11
             WHEN 'Ace' THEN 12
             END;

# Еще вариант

SELECT suit, rankvalue
FROM Ranks
         CROSS JOIN Suits
ORDER BY CASE suit
             WHEN 'Spades' THEN 1
             WHEN 'Clubs' THEN 2
             WHEN 'Diamonds' THEN 3
             WHEN 'Hearts' THEN 4
             END,
         CASE rankvalue
             WHEN 'Jack' THEN 11
             WHEN 'Queen' THEN 12
             WHEN 'King' THEN 13
             WHEN 'Ace' THEN 14
             ELSE CONVERT(rankvalue, SIGNED)
             END