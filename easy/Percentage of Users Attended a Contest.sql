select contest_id, 
ROUND((COUNT(u.user_id) / (select COUNT(u1.user_id) from users u1)) * 100, 2) as percentage
from Users u right join Register r
on u.user_id = r.user_id
group by contest_id 
order by percentage desc, contest_id
