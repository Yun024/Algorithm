/* https://solvesql.com/problems/monthly-author-candidates/ */

with temp as (
  select
  avg(case when genre = 'Fiction' then reviews end) avg_review
  from books
)

select
  author
from books
where genre = 'Fiction'
group by author
having count(author) >= 2
and avg(user_rating) >= 4.5
and avg(reviews) >= (select avg_review from temp)
order by author