## Url : https://solvesql.com/problems/max-row/

-- select id
-- from points
-- where x = (select max(x) from points)
-- or y = (select max(y) from points)

select A.id
from points A
inner join (select id, max(x) as max_x, max(y) as max_y from points) B
on A.x = B.max_x or A.y = B.max_y
order by A.id 
