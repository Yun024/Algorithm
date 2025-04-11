## Url : https://solvesql.com/problems/multiplatform-games/

-- with cte as(
-- select 
--   distinct g.name,
--   case when p.name in ('PS3','PS4','PSP','PSV') then 'Sony' end sony,
--   case when p.name in ('Wii','WiiU','DS','3DS') then 'Nintendo' end nintendo,
--   case when p.name in ('X360','XONE') then 'Microsoft' end platform
-- from games g
-- inner join platforms p on g.platform_id = p.platform_id
-- where g.year >=2012
-- and (sony is not null or nintendo is not null or platform is not null))

-- select name
-- from cte
-- group by name
-- having count(name) >= 2

with cte as (
select 
  distinct g.name,
  case when p.name in ('PS3','PS4','PSP','PSV') then 'Sony' 
  when p.name in ('Wii','WiiU','DS','3DS') then 'Nintendo'
  when p.name in ('X360', 'XONE') then 'Microsoft' end as platform
from games g
inner join platforms p on g.platform_id = p.platform_id
where year >= 2012
and platform is not null)

select 
  name
from cte
group by name
having count(platform) >= 2

