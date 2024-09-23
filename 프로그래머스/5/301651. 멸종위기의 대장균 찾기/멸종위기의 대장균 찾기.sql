-- 코드를 작성해주세요

with recursive ecoli_gen as(
    select id, parent_id, 1 as gen
    from ecoli_data 
    where parent_id is null
    
    union all
    
    select e.id, e.parent_id, g.gen+1 as gen
    from ecoli_data e, ecoli_gen g
    where g.id = e.parent_id
)

select count(*) count, a.gen generation 
from ecoli_gen a 
left join ecoli_data b
on a.id = b.parent_id
where b.id is null
group by a.gen 
order by generation asc