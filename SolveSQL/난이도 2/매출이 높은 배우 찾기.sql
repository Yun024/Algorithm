/* https://solvesql.com/problems/top-revenue-actors/ */

select
  a.first_name first_name,
  a.last_name last_name,
  sum(p.amount) total_revenue
from payment p
inner join rental r on p.rental_id = r.rental_id
inner join inventory i on r.inventory_id = i.inventory_id
inner join film f on i.film_id = f.film_id
inner join film_actor fa on f.film_id = fa.film_id
inner join actor a on fa.actor_id = a.actor_id
group by a.actor_id
order by total_revenue desc
limit 5;