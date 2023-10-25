-- 코드를 입력하시오
select 
to_number(to_char(sales_date,'YYYY')) year, 
to_number(to_char(sales_date,'MM')) month, 
count(distinct a.user_id) puchased_users, 
round(count(distinct a.user_id) / 
      (select  count(*) from user_info
       where to_char(joined,'YYYY')='2021'),1) puchased_ratio
from user_info a, online_sale b
where a.user_id = b.user_id 
and to_char(joined,'YYYY') = '2021'
group by to_char(sales_date,'YYYY') , to_char(sales_date,'MM')
order by year, month

