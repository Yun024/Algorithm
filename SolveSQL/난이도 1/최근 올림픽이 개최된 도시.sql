## Url : https://solvesql.com/problems/olympic-cities/

select year, upper(substring(city,1,3)) city
from games
where year >= 2000
order by year desc