-- 코드를 입력하세요
SELECT *
from food_product
where price = (select max(price) from food_product)
 
select *
from food_product
order by price desc limit 1
