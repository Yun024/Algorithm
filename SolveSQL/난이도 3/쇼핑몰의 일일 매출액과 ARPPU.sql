## Url : https://solvesql.com/problems/daily-arppu/

-- with olist_sales_statistics as (
-- select strftime('%Y-%m-%d',A.order_purchase_timestamp) dt, B.payment_value
-- from olist_orders_dataset A 
-- inner join 
--   (select order_id, sum(payment_value) payment_value
--   from olist_order_payments_dataset
--   group by order_id)  B on A.order_id = B.order_id
-- where dt >= '2018-01-01'
-- )

-- select dt, count(1) pu, round(sum(payment_value),2) revenue_daily, round(sum(payment_value)/count(1),2) arppu
-- from olist_sales_statistics
-- group by dt
-- order by dt 

select 
  strftime('%Y-%m-%d',A.order_purchase_timestamp) dt,
  count(distinct A.customer_id) pu,
  round(sum(B.payment_value),2) revenue_daily,
  round(sum(B.payment_value)/count(distinct A.customer_id),2) arppu
from olist_orders_dataset A
inner join olist_order_payments_dataset B on A.order_id = B.order_id
where dt >= '2018-01-01'
group by dt
order by dt