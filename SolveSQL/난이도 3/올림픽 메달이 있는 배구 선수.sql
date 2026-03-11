/* https://solvesql.com/problems/volleyball-players-with-medals/ */

select
  a.id as id,
  a.name as name,
  string_agg(r.medal,',') as medals 
from events e
inner join records r on e.id = r.event_id
inner join athletes a on r.athlete_id = a.id
inner join teams t on r.team_id = t.id
where e.event = 'Volleyball Women''s Volleyball'
and r.medal is not null
and t.team = 'KOR'
group by a.id, a.name
