## Url : https://solvesql.com/problems/find-unnecessary-station-2/

with rent as (
  select 
    rent_station_id,
    sum(case when strftime('%Y-%m',rent_at) = '2018-10' then 1 else 0 end) rent_2018,
    sum(case when strftime('%Y-%m',rent_at) = '2019-10' then 1 else 0 end) rent_2019
  from rental_history
  group by rent_station_id
),

return as (
  select 
    return_station_id,
    sum(case when strftime('%Y-%m',return_at) = '2018-10' then 1 else 0 end) return_2018,
    sum(case when strftime('%Y-%m',return_at) = '2019-10' then 1 else 0 end) return_2019
  from rental_history
  group by return_station_id
)

select 
  s.station_id station_id,
  s.name name,
  s.local local,
  round(100.0 * (r1.rent_2019 + r2.return_2019) / (r1.rent_2018 + r2.return_2018),2) as usage_pct
from station s
inner join rent r1 on s.station_id = r1.rent_station_id
inner join return r2 on s.station_id = r2.return_station_id
where usage_pct <= 50
and usage_pct != 0
