## Url : https://www.hackerrank.com/challenges/occupations/problem?isFullScreen=true

-- ------------------- use. CASE
-- with occupation_rn as
-- (select name, occupation, row_number() over(partition by occupation order by name) as rn
--  from occupations) 
                  
-- select 
-- max(case when occupation ='Doctor' then name else null end) as Doctor,
-- max(case when occupation ='Professor' then name else null end) as Professor,
-- max(case when occupation ='Singer' then name else null end) as Singer,
-- max(case when occupation ='Actor' then name else null end) as Actor
-- from occupation_rn
-- group by rn

-- -------------------- use. If
with occupation_rn as
(select name, occupation, row_number() over(partition by occupation order by name) as rn
 from occupations)
 
select 
max(if(occupation='Doctor',name,NULL)) as Doctor,
max(if(occupation='Professor',name,NULL)) as Professor,
max(if(occupation='Singer',name,NULL)) as Singer,
max(if(occupation='Actor',name,NULL)) as Actor
from occupation_rn
group by rn