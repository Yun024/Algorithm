#### 안시조인, 서브쿼리 사용, 선두컬럼에 to_char을 사용하여 비교 
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


#### 서브쿼리 사용x, between사용, 오라클 조인(join대신 where) 사용 

select A.category, sum(B.sales) total_sales
from book A , book_sales B
where A.book_id = B.book_id and
B.sales_date between to_date('2022-01-01','YYYY-MM-DD') and to_date('2022-01-31','YYYY-MM-DD') 
group by A.category
order by A.category
