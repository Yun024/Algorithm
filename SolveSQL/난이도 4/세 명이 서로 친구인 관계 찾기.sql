/* https://solvesql.com/problems/friend-group-of-3/ */

select
  e1.user_a_id as user_a_id,
  e1.user_b_id as user_b_id,
  e2.user_b_id as user_c_id
from edges e1
join edges e2 on e1.user_b_id = e2.user_a_id
join edges e3 
  on (e3.user_a_id = e2.user_b_id and e3.user_b_id = e1.user_a_id)
  or (e3.user_a_id = e1.user_a_id and e3.user_b_id = e2.user_b_id)
where e1.user_a_id < e1.user_b_id
and e1.user_b_id < e2.user_b_id
and 3820 in (e1.user_a_id, e1.user_b_id, e2.user_b_id)
