## Url : https://solvesql.com/problems/weekday-stats-airpollution/

select 
  case when strftime('%w',measured_at)='0' then '일요일' 
  when strftime('%w',measured_at)='1' then '월요일'
  when strftime('%w',measured_at)='2' then '화요일'
  when strftime('%w',measured_at)='3' then '수요일'
  when strftime('%w',measured_at)='4' then '목요일'
  when strftime('%w',measured_at)='5' then '금요일'
  else '토요일' end as weekday,
  round(avg(no2),4) no2,
  round(avg(o3),4) o3,
  round(avg(co),4) co,
  round(avg(so2),4) so2,
  round(avg(pm10),4) pm10,
  round(avg(pm2_5),4) pm2_5
from measurements
group by weekday
order by 
case when strftime('%w',measured_at)='0' then 1 else 0 end, strftime('%w',measured_at)
