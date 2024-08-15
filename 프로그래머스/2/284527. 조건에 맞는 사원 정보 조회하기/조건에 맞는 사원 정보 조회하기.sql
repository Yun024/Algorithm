-- 코드를 작성해주세요
### 동점자가 없을 경우 LIMIT를 사용해도 원하는 년도의 가장 높은 사원의 점수를 추출할 수 있음 
# select sum(score) as score, b.emp_no, emp_name, position, email 
# from hr_department a, hr_employees b, hr_grade c
# where a.dept_id = b.dept_id 
# and b.emp_no = c.emp_no
# and c.year = 2022
# group by b.emp_no, b.emp_name, b.position, b.email
# order by score desc limit 1;

### 동점자가 있을 경우 RANK함수를 사용

select score, emp_no, emp_name, position, email  from (
select rank() over(order by sum(score) desc) as rk , sum(score) as score, b.emp_no, emp_name, position, email
from hr_department a, hr_employees b, hr_grade c
where a.dept_id = b.dept_id 
and b.emp_no = c.emp_no
and c.year = 2022
group by b.emp_no, b.emp_name, b.position, b.email
) a
where rk =1