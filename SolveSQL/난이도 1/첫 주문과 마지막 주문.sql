## Url : https://solvesql.com/problems/first-and-last-orders/

select *
from (select date(order_purchase_timestamp) first_order_date
from olist_orders_dataset
order by order_purchase_timestamp 
limit 1) a,
(select date(order_purchase_timestamp) last_order_date
from olist_orders_dataset
order by order_purchase_timestamp desc
limit 1) b


-- select 
--   date(min(order_purchase_timestamp)) first_order_date,
--   date(max(order_purchase_timestamp)) last_order_date
-- from olist_orders_dataset
