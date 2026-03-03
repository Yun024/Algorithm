/* https://solvesql.com/problems/revenue-weekday-weekend/ */

select 
  case when day in ('Sun','Sat') then 'weekend'
  else 'weekday' end as week,
  sum(total_bill) as sales
from tips
group by week
order by sales desc;