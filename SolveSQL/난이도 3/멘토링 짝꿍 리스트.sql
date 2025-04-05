## Url : https://solvesql.com/problems/mentor-mentee-list/

select 
 A.employee_id mentee_id,
 A.name mentee_name,
 B.employee_id mentor_id,
 B.name mentor_name
from (select * from employees where join_date between '2021-10-01' and '2021-12-31') A 
inner join (select * from employees where join_date <= '2020-01-01') B on A.department != B.department
order by A.employee_id