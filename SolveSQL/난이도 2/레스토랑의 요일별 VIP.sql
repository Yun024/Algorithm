## Url : https://solvesql.com/problems/restaurant-vip/

with max_bill as (
  select max(total_bill)
  from tips
  group by day)

select *
from tips
where total_bill in (select * from max_bill)