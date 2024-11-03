## Url : https://www.hackerrank.com/challenges/weather-observation-station-20/problem?isFullScreen=true

-- with median as (
-- select lat_n, rank() over(order by lat_n) rk
-- from station)

-- select round(lat_n,4)
-- from median
-- where rk = (select round(max(rk)/2) from median)

with percent as(
select lat_n, percent_rank() over(order by lat_n) pr
from station)

select round(lat_n,4)
from percent
where pr = 0.5