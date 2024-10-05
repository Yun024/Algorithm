## Url : https://www.hackerrank.com/challenges/weather-observation-station-5/problem?isFullScreen=true

select city, len
from (
    select 
        city, 
        length(city) as len, 
        rank() over(order by length(city) desc, city asc) as max_rn,
        rank() over(order by length(city) asc, city asc)  as min_rn
    from station) a
where max_rn = 1
or min_rn = 1
order by city

----------------------------------

(select city, length(city)
from station
where length(city) = (select min(length(city)) from station)
order by city
limit 1)

union all

(select city, length(city)
from station
where length(city) = (select max(length(city)) from station)
order by city
limit 1)
