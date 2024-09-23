-- 코드를 작성해주세요
select a.dept_id, dept_name_en, round(avg(b.sal)) avg_sal 
from hr_department a, hr_employees b
where a.dept_id = b.dept_id 
group by dept_id 
order by avg_sal desc