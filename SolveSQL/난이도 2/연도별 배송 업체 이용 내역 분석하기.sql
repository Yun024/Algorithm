/* https://solvesql.com/problems/yearly-shipping-usage/ */

select
  extract(year from purchased_at) as year,
  sum(case when shipping_method = 'Standard' then 1 end) + 
  sum(case when is_returned = 'true' then 1 end) as standard,
  sum(case when shipping_method = 'Express' then 1 end) as Express,
  sum(case when shipping_method = 'Overnight' then 1 end) as Overnight
from transactions
where shipping_method is not null
group by year
order by year