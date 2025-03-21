## Url : https://solvesql.com/problems/high-season-of-restaurant/

with answer_day as(
  select day
  from tips
  group by day
  having sum(total_bill) >= 1500
)

select *
from tips
where day in (select day from answer_day)