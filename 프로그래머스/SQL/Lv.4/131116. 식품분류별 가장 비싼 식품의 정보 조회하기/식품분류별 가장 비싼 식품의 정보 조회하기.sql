-- 코드를 입력하세요
select A.category, A.price, A.product_name 
from food_product A, (
SELECT category, max(price) as price from food_product 
group by category having category in ('과자','국','김치','식용유')
) B
where A.category = B.category 
and A.price = B.price
order by A.price desc



