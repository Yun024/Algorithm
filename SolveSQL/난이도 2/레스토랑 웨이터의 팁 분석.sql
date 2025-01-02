## Url : https://solvesql.com/problems/tip-analysis/

select day, time, round(avg(tip),2) avg_tip, round(avg(size),2) avg_size
from tips
group by day, time
order by day, time

