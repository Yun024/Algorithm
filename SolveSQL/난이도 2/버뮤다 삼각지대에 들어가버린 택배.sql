## Url : https://solvesql.com/problems/shipment-in-bermuda/

select 
  strftime('%Y-%m-%d',order_delivered_carrier_date) delivered_carrier_date, count(1) orders
from olist_orders_dataset
where order_delivered_customer_date is null
and strftime('%Y-%m',order_delivered_carrier_date) = '2017-01'
group by strftime('%Y-%m-%d', order_delivered_carrier_date)
order by 1