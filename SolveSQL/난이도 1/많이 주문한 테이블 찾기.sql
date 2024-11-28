## Url : https://solvesql.com/problems/find-tables-with-high-bill/

select *
from tips
where total_bill > (
select avg(total_bill)
from tips)
