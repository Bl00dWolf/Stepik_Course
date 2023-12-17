SELECT SUBSTRING_INDEX(email, '@', -1)                                                                     AS domain,
       GROUP_CONCAT(SUBSTRING_INDEX(email, '@', 1) ORDER BY SUBSTRING_INDEX(email, '@', 1) SEPARATOR ', ') AS users
FROM Directors
GROUP BY domain
ORDER BY domain;