# Write your MySQL query statement below
select a.machine_id , round(avg(a1.timestamp - a.timestamp ), 3)   as processing_time 
from Activity as a
join Activity as a1
on a.activity_type = 'start'  and a1.activity_type = 'end' and a1.machine_id=a.machine_id and a1.process_id=a.process_id
group by a.machine_id     ;