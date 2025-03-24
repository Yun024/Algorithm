## Url : https://solvesql.com/problems/film-ending-with-consonant/

-- select title
-- from film
-- where rating in ('R','NC-17')
-- and title not like ('%A')
-- and title not like ('%E')
-- and title not like ('%I')
-- and title not like ('%O')
-- and title not like ('%U')

select title
from film
where rating in ('R','NC-17')
and title not regexp '[AEIOU]$'