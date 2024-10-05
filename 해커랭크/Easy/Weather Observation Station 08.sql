## Url : https://www.hackerrank.com/challenges/weather-observation-station-8/problem?isFullScreen=true

select distinct city
from station
-- left & right use
-- where left(city,1) in ('a','e','i','o','u')
-- and right(city,1) in ('a','e','i','o','u')
where city regexp '^[aeiou]'
and city regexp '[aeiou]$'
