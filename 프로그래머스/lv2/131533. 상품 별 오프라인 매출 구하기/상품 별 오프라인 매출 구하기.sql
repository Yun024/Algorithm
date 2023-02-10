-- 코드를 입력하세요
SELECT product_code, price * sum(sales_amount) as sales
from product 
inner join offline_sale    
using (product_id)
group by product_code
order by sales desc ,product_code
    
