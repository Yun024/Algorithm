/* https://solvesql.com/problems/volleyball-players-in-two-consecutive-olympics/ */

with temp as (
select
  g.year,
  lead(g.year,1) over(partition by a.id order by g.year) as lead_year,
  a.id,
  a.name
from records r 
inner join teams t on r.team_id = t.id
inner join events e on r.event_id = e.id
inner join athletes a on r.athlete_id = a.id
inner join games g on r.game_id = g.id
where t.team = 'KOR'
and e.event = 'Volleyball Women''s Volleyball'
order by a.name, g.year
)

select 
  distinct id, name
from temp
where lead_year - year = 4

