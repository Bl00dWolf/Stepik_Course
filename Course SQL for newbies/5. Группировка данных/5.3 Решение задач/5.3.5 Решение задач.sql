SELECT COUNT(IF(WEEKDAY(submit_date) IN ('5', '6'), 1, NULL))                AS weekend_count,
       COUNT(IF(WEEKDAY(submit_date) IN ('0', '1', '2', '3', '4'), 1, NULL)) AS working_count
FROM Actions