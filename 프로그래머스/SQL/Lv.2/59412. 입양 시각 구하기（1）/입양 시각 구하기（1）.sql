-- 코드를 입력하세요
SELECT date_format(datetime,"%H") hour, count(*) count
from animal_outs
group by hour
having hour > 08 and hour< 20
order by hour