-- 코드를 작성해주세요
select distinct a.id, a.email, a.first_name, a.last_name
from developers a, skillcodes b
where b.code & a.skill_code = b.code
and b.category = 'Front End'
order by id