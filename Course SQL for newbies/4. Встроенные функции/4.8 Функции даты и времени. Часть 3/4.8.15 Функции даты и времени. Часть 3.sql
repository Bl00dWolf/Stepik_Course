SELECT CONCAT(name, ' ', surname)                                                AS staffer,
       SUBTIME(TIMEDIFF(work_end, work_start), TIMEDIFF(break_end, break_start)) AS work_time
FROM Staff
ORDER BY work_time DESC, staffer;