## Url : https://solvesql.com/problems/inspection-needed-bike/

select bike_id
from rental_history 
where strftime('%Y-%m',rent_at) = '2021-01'
group by bike_id
having sum(distance) >= 50000
