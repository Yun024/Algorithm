-- 코드를 입력하세요
select *from(
select flavor
from(
select *
from july 

union all

select *
from first_half
)group by flavor
order by sum(total_order) desc
) where rownum < 4