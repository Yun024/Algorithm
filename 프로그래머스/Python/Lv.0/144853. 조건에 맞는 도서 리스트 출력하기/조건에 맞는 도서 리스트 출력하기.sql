-- 코드를 입력하세요
SELECT book_id, date_format(published_date,"%Y-%m-%d") published_date
from book
where year(published_date)="2021" and 
category like "인문"
order by published_date asc

# select book_id, published_date
# from book
# where left(published_date,4)= "2021" and
# category ="인문"
