## Url : https://www.hackerrank.com/challenges/symmetric-pairs/problem?isFullScreen=true

with rk_func as(
select x, y, row_number() over(order by x, y) rk
from functions)

select a.x, a.y
from rk_func a 
inner join rk_func b on a.x= b.y and a.y = b.x and a.rk !=  b.rk
where a.x <= a.y
group by a.x, a.y
order by a.x