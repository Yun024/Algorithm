/* https://solvesql.com/problems/count-stamps/ */

select
  case when total_bill >= 25 then 2
  when total_bill >= 15 then 1
  else 0 end as stamp, count(*) as count_bill
from tips
group by stamp
order by stamp;
