-- 코드를 입력하세요
select B.animal_id, B.name
from animal_ins A, animal_outs B
where A.animal_id(+) = B.animal_id
and A.animal_id is null
order by B.animal_id