## Url : https://solvesql.com/problems/best-working-day/

-- with max_tip as (
--   select max(tip) tip
--   from (
--   select sum(tip) tip
--   from tips
--   group by day))

-- select day, round(sum(tip),2) tip_daily
-- from tips
-- group by day
-- having sum(tip) = (select tip from max_tip)


select day, round(sum(tip),2) tip_daily
from tips
group by day
order by sum(tip) DESC
limit 1