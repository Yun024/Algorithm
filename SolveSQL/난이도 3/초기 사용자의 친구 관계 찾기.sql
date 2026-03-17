/* https://solvesql.com/problems/friendship-between-early-users/ */


-- with temp as (
--   select
--     rank() over(order by user_a_id+user_b_id) as rk,
--     user_a_id,
--     user_b_id,
--     user_a_id + user_b_id id_sum
--   from edges)

-- select
--   user_a_id,
--   user_b_id,
--   id_sum
-- from temp
-- where rk*1.0/(select count(1) from edges) <= 0.001

-- with temp as (
--   select 
--     round(count(1)*0.001) as cnt
--   from edges
-- )

-- select
--   user_a_id,
--   user_b_id,
--   (user_a_id + user_b_id) id_sum
-- from edges
-- order by id_sum
-- limit (select cnt from temp);)

with temp as (
  select
    user_a_id,
    user_b_id,
    (user_a_id + user_b_id) id_sum,
    percent_rank() over(order by user_a_id+user_b_id) as pr
  from
    edges)

select
  user_a_id,
  user_b_id,
  id_sum
from temp
where pr <= 0.001