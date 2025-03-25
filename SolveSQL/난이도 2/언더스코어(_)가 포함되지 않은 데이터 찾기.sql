## Url : https://solvesql.com/problems/data-without-underscore/

select distinct page_location
from ga
-- where page_location not like '%\_%' ESCAPE '\'
where page_location not regexp '_'