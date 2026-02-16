## Url: https://solvesql.com/problems/movies-about-love/

select title, year, rotten_tomatoes
from movies
where title like '%Love%' or title like '%love%'
order by rotten_tomatoes desc,
year desc ;