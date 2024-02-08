SELECT Playback.id AS session_id
FROM Playback
         LEFT JOIN Ads ON Playback.user_id = Ads.user_id AND
                          (Ads.time_stamp BETWEEN Playback.start_time AND Playback.end_time)
WHERE Ads.id IS NULL
ORDER BY Playback.id