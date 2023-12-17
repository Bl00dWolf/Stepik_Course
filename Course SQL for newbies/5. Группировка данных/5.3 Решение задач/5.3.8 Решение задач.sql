SELECT DISTINCT viewer_id
FROM Views
GROUP BY viewer_id, view_date
HAVING COUNT(DISTINCT article_id) >= 2
ORDER BY viewer_id
