## Url : https://www.hackerrank.com/challenges/placements/problem?isFullScreen=true

select a.name
from students a 
inner join friends b on a.id = b.id 
inner join packages c on a.id = c.id
inner join packages d on b.friend_id = d.id
where c.salary < d.salary
order by d.salary