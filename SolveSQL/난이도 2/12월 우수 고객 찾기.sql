/* https://solvesql.com/problems/whales-of-december/ */

select customer_id
from records
where extract (month from order_date) = 12
group by customer_id
having sum(sales) >= 1000;