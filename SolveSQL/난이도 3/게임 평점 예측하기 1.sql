## Url : https://solvesql.com/problems/predict-game-scores-1/

with re_value as (
select 
  genre_id, 
  round(avg(critic_score),3) critic_score,
  ceil(avg(critic_count)) critic_count,
  round(avg(user_score),3) user_score,
  ceil(avg(user_count)) user_count
from games
group by genre_id)

select 
  g.game_id,
  g.name,
  coalesce(g.critic_score,r.critic_score) critic_score,
  coalesce(g.critic_count,r.critic_count) critic_count,
  coalesce(g.user_score,r.user_score) user_score,
  coalesce(g.user_count,r.user_count) user_count
from games g
inner join re_value r on g.genre_id = r.genre_id
where year >= 2015
and (g.critic_score is null or g.critic_count is null or g.user_score is null or g.user_count is null)


-- with re_value as (
-- select 
--   genre_id, 
--   round(avg(critic_score),3) critic_score,
--   ceil(avg(critic_count)) critic_count,
--   round(avg(user_score),3) user_score,
--   ceil(avg(user_count)) user_count
-- from games
-- group by genre_id),

-- left_table as (
--   select 
--     game_id,
--     genre_id,
--     name,
--     critic_score,
--     critic_count,
--     user_score,
--     user_count
--   from games
--   where year >= 2015
--   and (critic_score is null or critic_count is null or user_score is null or user_count is null)
-- )

-- select 
--   l.game_id,
--   l.name,
--   case when l.critic_score is null then r.critic_score else l.critic_score end as critic_score,
--   case when l.critic_count is null then r.critic_count else l.critic_count end as critic_count,
--   case when l.user_score is null then r.user_score else l.user_score end as user_score,
--   case when l.user_count is null then r.user_count else l.user_count end as user_count
-- from left_table l
-- inner join re_value r on l.genre_id = r.genre_id






