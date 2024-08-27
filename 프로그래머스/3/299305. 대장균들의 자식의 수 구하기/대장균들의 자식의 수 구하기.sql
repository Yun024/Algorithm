-- 코드를 작성해주세요
select b.id, ifnull(child_count,0) child_count from (
select parent_id, count(*) child_count
from ecoli_data
where parent_id is not null
group by parent_id ) a 
right outer join 
(select id from ecoli_data) b
on a.parent_id = b.id
order by b.id 
