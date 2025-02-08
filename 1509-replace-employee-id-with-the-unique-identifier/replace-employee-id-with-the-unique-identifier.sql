# Write your MySQL query statement below

select euni.unique_id , e.name   
from Employees e
left JOIN EmployeeUNI euni
ON e.id = euni.id;