## Url : https://solvesql.com/problems/join/

-- select distinct(sport)
-- from events
-- where sport like 'G%'

select distinct athlete_id
from events e 
inner join records r on e.id = r.event_id
where e.sport ='Golf'


