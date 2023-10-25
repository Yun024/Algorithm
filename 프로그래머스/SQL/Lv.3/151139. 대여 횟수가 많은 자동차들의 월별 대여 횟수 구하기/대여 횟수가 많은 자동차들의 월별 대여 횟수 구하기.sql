-- 코드를 입력하세요
select to_number(to_char(start_date,'MM')) month , car_id, count(*) records
from car_rental_company_rental_history
where car_id in (
select car_id
from car_rental_company_rental_history
where start_date between to_date('2022-08-01','YYYY-MM-DD') and to_date('2022-10-31','YYYY-MM-DD')
group by car_id 
having count(car_id)>=5
)
and start_date between to_date('2022-08-01','YYYY-MM-DD') and to_date('2022-10-31','YYYY-MM-DD')
group by to_char(start_date,'MM'), car_id
having count(*)>0
order by to_char(start_date,'MM') , car_id desc