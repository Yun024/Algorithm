## Url : https://solvesql.com/problems/find-christmas-games/

select game_id, name, year
from games
where name like '%Christmas%' or name like '%Santa%'