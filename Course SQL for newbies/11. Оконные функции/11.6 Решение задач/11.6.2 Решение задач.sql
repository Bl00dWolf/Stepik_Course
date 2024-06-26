SELECT *,
       AVG(quantity)
           OVER (PARTITION BY user_id ORDER BY day RANGE BETWEEN INTERVAL 2 DAY PRECEDING AND CURRENT ROW) as three_day_moving_avg_quantity
FROM Posts;