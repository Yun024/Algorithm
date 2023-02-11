-- 코드를 입력하세요
SELECT A.name, A.datetime
from animal_ins as A
left join animal_outs as B 
on A.animal_id = B.animal_id
where B.animal_type is null
order by A.datetime limit 3