## Url : https://solvesql.com/problems/number-of-friends/

with cte as (
select user_a_id, user_b_id
from edges

union ALL

select user_b_id user_a_id, user_a_id user_b_id
from edges)

select u.user_id user_id, ifnull(c.num_friends,0) num_friends
from users u 
left join (
select user_a_id user_id, count(1) num_friends
from cte
group by user_a_id) c on u.user_id = c.user_id
order by 2 desc, 1


