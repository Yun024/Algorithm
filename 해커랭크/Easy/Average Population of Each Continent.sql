## Url : https://www.hackerrank.com/challenges/average-population-of-each-continent/problem?isFullScreen=true

select b.continent, floor(avg(a.population),0)
from city a, country b
where a.countrycode = b.code
group by b.continent