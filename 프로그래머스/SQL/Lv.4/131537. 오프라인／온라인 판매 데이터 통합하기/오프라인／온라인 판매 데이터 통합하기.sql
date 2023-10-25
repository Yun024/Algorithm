-- 코드를 입력하세요
select to_char(sales_date,'YYYY-MM-DD') sales_date, product_id, user_id, sales_amount
from(
select *
from online_sale 

union all 

select offline_sale_id, NULL user_id, product_id, sales_amount, sales_date
from offline_sale)
where to_char(sales_date,'YYYY-MM') = '2022-03'
order by sales_date, product_id, user_id
