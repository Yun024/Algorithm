## Url : https://www.hackerrank.com/challenges/earnings-of-employees/problem?isFullScreen=true

-- select months * salary, count(*)
-- from employee
-- where months * salary = (select max(months * salary) from employee )
-- group by months * salary

select months * salary, count(*)
from employee
group by months* salary
order by months* salary desc limit 1
