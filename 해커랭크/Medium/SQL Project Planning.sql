## Url : https://www.hackerrank.com/challenges/sql-projects/problem?isFullScreen=true

with recursive rf as(
select start_date, end_date, 1 as n
from projects a

union all

select b.start_date, a.end_date, n+1
from rf a
inner join projects b on a.start_date = b.end_date
)

select b.start_date, max(b.end_date)
from projects a
right outer join rf b on a.end_date = b.start_date
where a.start_date is null
group by b.start_date
order by max(n), b.start_date 

