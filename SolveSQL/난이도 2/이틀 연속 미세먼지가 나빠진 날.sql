/* https://solvesql.com/problems/bad-finddust-days-in-a-row/ */

with temp as (
select 
  lag(pm10,1) over(order by measured_at) as prev_pm10,
  pm10,
  lead(pm10,1) over(order by measured_at) as next_pm10,
  lead(measured_at,1) over(order by measured_at) as next_day
from measurements)

select
  next_day as date_alert
from temp
where prev_pm10 < pm10 and pm10 < next_pm10 and next_pm10 >= 30;