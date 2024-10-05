## Url : https://www.hackerrank.com/challenges/weather-observation-station-6/problem?isFullScreen=true

select distinct city
from station
#where city regexp('^a|^e|^i|^o|^u')
#where left(city,1) in ('a','e','i','o','u')
where city regexp '^[aeiou]'
