select Department, Employee, Salary 
from (
  select d.name as Department,
        e.name as Employee,
        Salary,
        DENSE_RANK() over(partition by d.name order by salary desc) as DN 
  from Employee e join Department d
  on e.departmentId = d.id 
) as temp
where DN between 1 and 3
