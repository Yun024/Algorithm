## Url : https://solvesql.com/problems/estimated-delivery-date/

select 
  strftime('%Y-%m-%d',order_purchase_timestamp) purchase_date,
  sum(case when order_delivered_customer_date < order_estimated_delivery_date then 1 else 0 end) as success,
  sum(case when order_delivered_customer_date >= order_estimated_delivery_date then 1 else 0 end) as fail
from olist_orders_dataset
where strftime('%Y-%m',order_purchase_timestamp) = '2017-01'
and order_estimated_delivery_date is not null
and order_delivered_customer_date is not null
group by purchase_date
order by purchase_date