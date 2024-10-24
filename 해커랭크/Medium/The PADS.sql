## Url : https://www.hackerrank.com/challenges/the-pads/problem?isFullScreen=true

-- select name from (
-- select concat(name,"(",left(occupation,1),")") as name, rank() over(order by name) as rk, 1 as bb
-- from occupations

-- union all

-- select concat('There are a total of ',count(*),' ',lower(occupation),'s.') as name, rank() over(order by count(*),occupation) as rk, 2 as bb
-- from occupations 
-- group by occupation) c
-- order by bb, rk 

select concat(name,"(",left(occupation,1),")") as name
from occupations

union all

select concat('There are a total of ',count(*),' ',lower(occupation),'s.') as name
from occupations
group by occupation

order by name 