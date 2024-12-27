## Url : https://solvesql.com/problems/count-stations/

select local, count(local) num_stations
from station
group by local
order by num_stations