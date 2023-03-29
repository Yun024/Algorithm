-- 코드를 입력하세요
SELECT C.car_id
from car_rental_company_car C inner join car_rental_company_rental_history R
on C.car_id = R.car_id
where car_type = '세단'
and to_char(start_date,'YYYY-MM') = '2022-10'
group by C.car_id
order by car_id desc