select project_id, ROUND(AVG(experience_years), 2) as average_years
from Employee e inner join Project p
on e.employee_id = p.employee_id 
group by project_id
