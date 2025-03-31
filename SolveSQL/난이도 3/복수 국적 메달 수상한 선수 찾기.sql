## Url : https://solvesql.com/problems/multiple-medalist/

-- with group_records as (
-- select a.id
-- from records r 
-- inner join athletes a on r.athlete_id = a.id
-- inner join games g on r.game_id = g.id
-- inner join teams t on r.team_id = t.id
-- where g.year >= 2000
-- and r.medal is not null
-- group by a.id, t.team) ,

-- answer_id as (
--   select *
--   from group_records
--   group by id
--   having count(id) >=2 
-- )

-- select B.name
-- from answer_id A
-- inner join athletes B on A.id = B.id
-- order by B.name

select a.name
from records r 
inner join athletes a on r.athlete_id = a.id
inner join games g on r.game_id = g.id
where medal is not NULL
and g.year >= 2000
group by a.id
having count(distinct r.team_id) >= 2
order by a.name