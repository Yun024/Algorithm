-- 코드를 입력하세요

select a.hour hour, nvl(count,0) count
from (
select to_char(level,'00')-1 hour
from dual connect by level <=24 ) a,
(select to_char(datetime,'HH24') hour,count(*) count
from animal_outs
group by to_char(datetime,'HH24') ) b
where a.hour =b.hour(+)
order by a.hour