## Url : https://solvesql.com/problems/daily-revenue/

select day, sum(total_bill) revenue_daily
from tips
group by day
having sum(total_bill) >= 1000
order by revenue_daily desc