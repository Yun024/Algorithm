-- 코드를 입력하세요
select extract(year from sales_date) year, extract(month from sales_date) month,gender, count(distinct A.user_id) users
from user_info A, online_sale B
where A.user_id = B.user_id
and gender is not null
group by extract(year from sales_date), extract(month from sales_date), gender
order by year, month, gender

