/* https://solvesql.com/problems/ab-testing-buckets-2/ */

with t1 as(
select
  case when customer_id % 10 = 0 then 'A'
  else 'B' end as bucket,
  customer_id,
  transaction_id,
  total_price
from transactions
where is_returned = 'false')

select
  bucket,
  count(distinct customer_id) user_count,
  round(count(transaction_id)*1.0/count(distinct customer_id),2) avg_orders,
  round(sum(total_price)/count(distinct customer_id),2) as avg_revenue
from t1
group by bucket;