select * from (
select 
case 
    when sk_nm regexp 'Python' and sk_cat regexp 'Front End' then 'A'
    when sk_nm regexp 'C#' then 'B'
    when sk_cat regexp 'Front End' then 'C'
    else null
end as grade,
id, email
from (
    select 
    group_concat(name separator ',') as sk_nm,
    group_concat(category separator ',') as sk_cat,
    id, email
    from developers a, skillcodes b
    where a.skill_code & b.code != 0 
    group by id, email
) a) b
where grade is not null
order by grade, id asc