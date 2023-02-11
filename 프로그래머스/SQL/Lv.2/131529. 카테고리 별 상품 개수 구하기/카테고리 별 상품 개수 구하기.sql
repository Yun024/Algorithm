-- 코드를 입력하세요
SELECT left(product_code,2) category, count(left(product_code,2)) products
from product
group by left(product_code,2)