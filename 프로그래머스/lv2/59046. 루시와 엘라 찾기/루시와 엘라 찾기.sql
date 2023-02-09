-- 코드를 입력하세요
select animal_id, name, sex_upon_intake
from animal_ins
where name in ("Lucy","Ella","Pickle","Rogan","Sabrina","Mitty")
order by animal_id

# 정규표현식으로 할거면 ^와$을 통해 시작과 끝을 표시해주어야 한다. 
# SELECT animal_id, name, sex_upon_intake
# from animal_ins
# where name regexp "^(Lucy|Ella|Pickle|Rogan|Sabrina|Mitty$)$"
# order by animal_id