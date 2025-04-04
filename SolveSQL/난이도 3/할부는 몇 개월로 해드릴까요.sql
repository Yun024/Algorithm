## Url : https://solvesql.com/problems/installment-month/

select 
  payment_installments,
  count(distinct order_id) order_count,
  min(payment_value) min_value,
  max(payment_value) max_value,
  avg(payment_value) avg_value
from olist_order_payments_dataset
where payment_type = 'credit_card'
group by payment_installments
