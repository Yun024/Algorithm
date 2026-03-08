/* https://solvesql.com/problems/dvdrental-vip/ */

select c.customer_id
from rental r inner join customer c 
on r.customer_id = c.customer_id
where c.active = 'true'
group by c.customer_id
having count(c.customer_id) >= 35
