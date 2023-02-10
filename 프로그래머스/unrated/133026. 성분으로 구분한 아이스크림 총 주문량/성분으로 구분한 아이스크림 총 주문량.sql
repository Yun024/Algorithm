-- 코드를 입력하세요
SELECT ingredient_type, sum(total_order) total_order
from first_half
inner join icecream_info 
using (flavor)
group by ingredient_type
order by total_order 