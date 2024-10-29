## Url : https://www.hackerrank.com/challenges/the-company/problem?isFullScreen=true

-- select 
--     a.company_code, 
--     a.founder, 
--     count(distinct b.lead_manager_code), 
--     count(distinct c.senior_manager_code),
--     count(distinct d.manager_code),
--     count(distinct e.employee_code)    
-- from company a,
--     lead_manager b, 
--     senior_manager c, 
--     manager d, 
--     employee e
-- where a.company_code = b.company_code
-- and b.lead_manager_code = c.lead_manager_code
-- and c.senior_manager_code = d.senior_manager_code
-- and d.manager_code = e.manager_code
-- group by a.company_code, a.founder
-- order by a.company_code


select  
    a.company_code, 
    a.founder, 
    count(distinct b.lead_manager_code), 
    count(distinct c.senior_manager_code),
    count(distinct d.manager_code),
    count(distinct e.employee_code)
from company a 
    inner join lead_manager b on a.company_code = b.company_code
    inner join senior_manager c on b.lead_manager_code = c.lead_manager_code
    inner join manager d on c.senior_manager_code = d.senior_manager_code
    inner join employee e on d.manager_code = e.manager_code
group by a.company_code, a.founder
order by a.company_code