## Url : https://solvesql.com/problems/finedust-seasonal-summary/

with season_measure as (
select 
  case when measured_at between '2022-03-01' and '2022-05-31' then 'spring'
  when measured_at between '2022-06-01' and '2022-08-31' then 'summer'
  when measured_at between '2022-09-01' and '2022-11-30' then 'autumn'
  else 'winter' end as season,
  pm10
from measurements)

select 
  season,
  median(pm10) pm10_median,
  round(avg(pm10),2) pm10_average
from season_measure
group by season
