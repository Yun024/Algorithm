-- 코드를 입력하세요
SELECT P.product_id, P.product_name, sum(O.amount)* P.price as total_sales
from food_product P, food_order O 
where P.product_id = O.product_id
and O.produce_date between to_date('2022-05-01','YYYY-MM-DD') and to_date('2022-05-31','YYYY-MM-DD')
group by P.product_id, P.product_name, P.price
order by total_sales desc, product_id


