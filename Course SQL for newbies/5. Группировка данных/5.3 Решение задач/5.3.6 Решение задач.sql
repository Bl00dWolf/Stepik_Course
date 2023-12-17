SELECT ad_id,
       COALESCE(
               ROUND(
                       ((SUM(IF(action = 'clicked', 1, 0)) /
                         (SUM(IF(action = 'clicked', 1, 0)) + SUM(IF(action = 'viewed', 1, 0)))) * 100), 2),
               0.00) AS rating
FROM Actions
GROUP BY ad_id
ORDER BY rating DESC;

# Еще вариант
# SELECT ad_id,
#        COALESCE(ROUND((SUM(CASE WHEN action = 'clicked' THEN 1 END) /
#                        (SUM(CASE WHEN action IN ('clicked', 'viewed') THEN 1 END))) * 100, 2), 0.00) AS rating
# FROM Actions
# GROUP BY ad_id
# ORDER BY rating DESC
