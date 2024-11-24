## Url : https://solvesql.com/problems/settled-sellers-1/

SELECT seller_id, count(distinct(order_id)) orders
FROM olist_order_items_dataset
GROUP BY SELLER_ID
HAVING COUNT(distinct(order_id)) >= 100