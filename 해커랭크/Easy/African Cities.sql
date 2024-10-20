## Url : https://www.hackerrank.com/challenges/african-cities/problem?isFullScreen=true

select a.name
from city a, country b
where a.countrycode = b.code
and b.continent = 'Africa'