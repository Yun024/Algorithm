-- 코드를 입력하세요
select category, sum(sales) total_sales
from 
(
    select *
    from book A inner join book_sales B
    on A.book_id = B.book_id
    where to_char(B.sales_date,'YYYY-MM') = '2022-01'
 )
group by category
order by category


-- select * 
-- from book A , book_sales B
-- where A.book_id = B.book_id