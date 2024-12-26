## Url : https://solvesql.com/problems/inspect-penguins/

select island, species
from penguins
group by island, species
order by island, species