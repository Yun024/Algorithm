## Url : https://solvesql.com/problems/bad-finedust-measure/

-- with next_measure as (
-- select row_number() over(order by measured_at) as rn, measured_at as next_day, pm10 as next_pm10
-- from measurements
-- where measured_at <> '2022-01-01'
-- )

-- select today, next_day, pm10, next_pm10 from (
-- select row_number() over(order by measured_at) as rn, measured_at as today, pm10
-- from measurements) A
-- inner join next_measure B on A.rn = B.rn 
-- where pm10 < next_pm10


with answer as(
select
  measured_at as today,
  lead(measured_at) over(order by measured_at) as next_day,
  pm10,
  lead(pm10) over(order by measured_at) as next_pm10
from measurements)

select *
from answer
where pm10 < next_pm10
