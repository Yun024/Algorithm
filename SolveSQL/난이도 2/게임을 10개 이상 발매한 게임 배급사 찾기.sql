## Url : https://solvesql.com/problems/publisher-with-many-games/

select B.name
from games A
inner join companies B on A.publisher_id = B.company_id
group by B.name
having count(B.name) >= 10
