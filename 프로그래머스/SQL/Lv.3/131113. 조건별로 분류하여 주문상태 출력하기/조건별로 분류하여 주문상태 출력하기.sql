-- 코드를 입력하세요
select order_id,product_id,to_char(out_date,'YYYY-MM-DD') out_date, 
case
    when out_date - to_date('2022-05-01','YYYY-MM-DD') <= 0 then '출고완료' 
    when out_date - to_date('2022-05-01','YYYY-MM-DD') > 0 then '출고대기' 
    else '출고미정'
    end 출고여부
from food_order
order by order_id 

