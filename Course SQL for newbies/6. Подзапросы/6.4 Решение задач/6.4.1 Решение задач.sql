SELECT ROUND(IFNULL(
                     (SELECT COUNT(DISTINCT requester_id, accepter_id)
                      FROM RequestsAccepted)
                         /
                     (SELECT COUNT(DISTINCT sender_id, send_to_id)
                      FROM FriendRequests), 0), 2) AS accept_rate