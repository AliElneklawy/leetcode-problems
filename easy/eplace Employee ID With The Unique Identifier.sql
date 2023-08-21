# Write your MySQL query statement below

select unique_id, name
from EmployeeUNI right outer join Employees
on EmployeeUNI.id = Employees.id
