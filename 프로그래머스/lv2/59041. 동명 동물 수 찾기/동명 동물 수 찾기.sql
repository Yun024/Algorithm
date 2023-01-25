-- 코드를 입력하세요
SELECT name, count(name) count
from animal_ins
group by name
having count(name)>1 and name is not null
order by name
