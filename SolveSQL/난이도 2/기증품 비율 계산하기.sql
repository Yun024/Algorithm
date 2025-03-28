## Url : https://solvesql.com/problems/ratio-of-gifts/

select 
 round(100.0 * sum(case when credit like '%gift%' then 1 end) / count(1),3) as ratio
from artworks


