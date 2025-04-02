## Url : https://solvesql.com/problems/characteristics-of-orders/

-- with records_dupl as (
--   select 
--     distinct(order_id),
--     region,
--     category
--   from 
--     records
-- )

-- select 
--   region as Region, 
--   sum(case when category = 'Furniture' then 1 else 0 end) as Furniture,
--   sum(case when category = 'Office Supplies' then 1 else 0 end) as [Office Supplies],
--   sum(case when category = 'Technology' then 1 else 0 end) as Technology
--   from records_dupl
-- group by region
-- order by region


select 
  region as Region,
  count(distinct(case when category='Furniture' then order_id else null end)) as Furniture,
  count(distinct(case when category='Office Supplies' then order_id else null end)) as [Office Supplies],
  count(distinct(case when category='Technology' then order_id else null end)) as Technology
from records
group by region
order by region