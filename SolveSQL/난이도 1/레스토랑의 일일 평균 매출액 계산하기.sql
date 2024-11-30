## Url : https://solvesql.com/problems/sales-summary/

-- select round(sum(total_bill)/count(distinct day),2) avg_sales
-- from tips


select round(avg(sales),2) avg_sales from(
select sum(total_bill) sales
from tips
group by day) a