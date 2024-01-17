SELECT followee AS user, COUNT(follower) AS followers
FROM Follow AS F
WHERE (SELECT COUNT(follower)
       FROM Follow
       WHERE F.followee = followee) >= 1
  AND followee IN (SELECT follower
                   FROM Follow)
GROUP BY followee
ORDER BY user;