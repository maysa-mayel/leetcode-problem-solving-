# Write your MySQL query statement below
delete  p 
from Person p
join Person p2
on p.email=p2.email and p2.id < p.id;