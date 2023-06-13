-- 코드를 입력하세요
select author_id, max(author_name) author_name, category, sum(total_sales) total_sales
from(
select a.author_id, author_name, category, price * sales total_sales
from book a, author b, book_sales c
where a.book_id = c.book_id
and a.author_id = b.author_id
and sales_date between to_date('2022-01-01','YYYY-MM-DD') and to_date('2022-01-31','YYYY-MM-DD')
) group by author_id, category
order by author_id, category desc