## Url : https://www.hackerrank.com/challenges/weather-observation-station-13/problem?isFullScreen=true

select round(sum(lat_n),4)
from station
-- where lat_n between 38.7880 and 137.2345
where lat_n > 38.7880 and lat_n < 137.2345
