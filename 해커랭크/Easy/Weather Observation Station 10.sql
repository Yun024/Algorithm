## Url : https://www.hackerrank.com/challenges/weather-observation-station-10/problem?isFullScreen=true

select distinct city
from station
-- where right(city,1) not in ('a','e','i','o','u')
where city not regexp '[aeiou]$'

