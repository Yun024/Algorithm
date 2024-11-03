## Url : https://www.hackerrank.com/challenges/the-report/problem?isFullScreen=true

select 
case when marks <= 69 then null
else name end as name, 
case when marks >= 90 then 10
when marks >= 80 then 9
when marks >= 70 then 8
when marks >= 60 then 7
when marks >= 50 then 6
when marks >= 40 then 5
when marks >= 30 then 4
when marks >= 20 then 3
when marks >= 10 then 2
else 1 end as grade,
marks
from students
order by grade desc, name, marks asc