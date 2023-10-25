-- 코드를 입력하세요
SELECT A.animal_id, A.name
from animal_ins A, animal_outs B
where A.animal_id = B.animal_id
and B.datetime - A.datetime <0
order by A.datetime 