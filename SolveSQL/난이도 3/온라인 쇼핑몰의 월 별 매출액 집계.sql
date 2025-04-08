## Url : https://solvesql.com/problems/shoppingmall-monthly-summary/

select 
  strftime('%Y-%m',a.order_date) order_month, 
  sum(case when a.order_id not like 'C%' then b.price * b.quantity end) ordered_amount,
  sum(case when a.order_id like 'C%' then b.price * b.quantity end) canceled_amount,
  sum(b.price * b.quantity) total_amount
from orders a
inner join order_items b on a.order_id = b.order_id
group by order_month
order by order_month
