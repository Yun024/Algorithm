-- 코드를 입력하세요

select I.animal_id, I.animal_type, I.name 
from animal_ins I, animal_outs O
where I.animal_id = O.animal_id
and sex_upon_intake like '%Intact%'
and sex_upon_outcome not like '%Intact%'
order by I.animal_id