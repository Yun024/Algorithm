## Url : https://solvesql.com/problems/olist-daily-revenue/

SELECT strftime('%Y-%m-%d', A.order_purchase_timestamp) dt, ROUND(SUM(B.payment_value),2) revenue_daily
FROM olist_orders_dataset A 
INNER JOIN olist_order_payments_dataset B ON A.order_id = B.order_id
GROUP BY strftime('%Y-%m-%d', A.order_purchase_timestamp)
HAVING dt >= '2018-01-01'
ORDER BY dt