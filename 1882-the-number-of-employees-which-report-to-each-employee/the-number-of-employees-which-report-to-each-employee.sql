select m.employee_id, m.name , e.reports_count , e.average_age 
from ( 
        select reports_to , count(reports_to )as reports_count, round(avg(age))as average_age 
        from Employees 
        group by reports_to 
        having count(reports_to )>=1) as e
left join Employees as m
on m.employee_id = e.reports_to
order by m.employee_id ;