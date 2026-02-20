/* https://solvesql.com/problems/yearly-net-sales/ */

select extract(year from purchased_at) as year, sum(total_price - discount_amount) as net_sales
from transactions
where is_returned = 'false'
group by extract(year from purchased_at)
order by year