SELECT MAX(num) AS num 
FROM MyNumbers
where num in
  (
  select *
  from MyNumbers
  group by num
  having count(*) = 1 
  )
