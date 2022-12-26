-- 코드를 입력하세요
select A.flavor
from first_half A
    left join icecream_info B
    on A.flavor = B.flavor
where total_order > 3000 and
ingredient_type ="fruit_based"
order by total_order desc