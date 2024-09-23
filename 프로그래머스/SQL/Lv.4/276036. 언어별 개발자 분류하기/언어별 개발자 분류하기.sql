### Group_concat 사용 
# select 
# case 
#     when group_concat(name) regexp 'Python' and group_concat(category) regexp 'Front End' then 'A'
#     when group_concat(name) regexp 'C#' then 'B'
#     when group_concat(category) regexp 'Front End' then 'C'
#     else null
# end as grade,
# id,
# email
# from developers a, skillcodes b
# where a.skill_code & b.code != 0 
# group by email, id
# having grade is not null
# order by grade, id

### group_concat 미사용 및 이중 when 사용 
select 
case 
    when sum(case when b.name = 'Python' then 10000 
             when b.category ='Front End' then 1 else 0 end) > 10000 then 'A'
    when sum(case when b.name ='C#' then 1 else 0 end ) > 0 then 'B'
    when sum(case when b.category = 'Front End' then 1 else 0 end) > 0 then 'C'
    else null
end as grade,
id,
email
from developers a, skillcodes b
where a.skill_code & b.code != 0 
group by id, email
having grade is not null
order by grade, id 
