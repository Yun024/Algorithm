## Url : https://solvesql.com/problems/top-3-bill/

with cte as (
  select row_number() over(partition by day order by total_bill desc) as rn,
  sex, time, total_bill, day from tips)

select 
  day,
  time,
  sex,
  total_bill
from cte 
where rn <= 3




