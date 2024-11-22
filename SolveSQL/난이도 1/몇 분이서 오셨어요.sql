## Url : https://solvesql.com/problems/size-of-table/

select *
from tips
where mod(size,2) = 1
-- where size % 2 = 1