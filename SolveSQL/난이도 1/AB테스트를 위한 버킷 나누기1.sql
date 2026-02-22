/* https://solvesql.com/problems/ab-testing-buckets-1/ */

select 
  distinct(customer_id),
  case when customer_id%10 = 0 then 'A'
  else 'B' end as bucket
from transactions
order by customer_id
