-- 코드를 작성해주세요
with pl as 
(select id, parent_id from ecoli_data)

select c.id
from pl a, pl b, pl c
where a.id = b.parent_id 
and b.id = c.parent_id 
and a.parent_id is null
order by c.id