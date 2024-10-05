## Url : https://www.hackerrank.com/challenges/weather-observation-station-9/problem?isFullScreen=true

select distinct city
from station
-- where left(city,1) not in ('a','e','i','o','u')
where city not regexp '^[aeiou]'

