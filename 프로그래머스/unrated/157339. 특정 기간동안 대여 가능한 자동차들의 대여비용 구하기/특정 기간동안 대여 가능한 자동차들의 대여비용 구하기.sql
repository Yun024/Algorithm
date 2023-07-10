select a.car_id car_id, max(a.car_type) car_type, (avg(daily_fee) - avg(daily_fee) * avg(discount_rate) / 100) * 30 fee
from car_rental_company_car a, car_rental_company_rental_history b, car_rental_company_discount_plan c 
where a.car_id = b.car_id
and a.car_type= c.car_type 
and a.car_type in ('세단','SUV')
and c.duration_type = '30일 이상'
and a.car_id not in(select distinct a.car_id
                    from car_rental_company_car a, car_rental_company_rental_history b, car_Rental_company_discount_plan c 
                    where a.car_id = b.car_id
                    and a.car_type = c.car_type
                    and (start_date < to_date('2022-11-01 00','YYYY-MM-DD HH24') and end_date > to_date('2022-10-31 23','YYYY-MM-DD HH24')))
group by a.car_id
having (avg(daily_fee) - avg(daily_fee) * avg(discount_rate) / 100) * 30 >= 500000
and (avg(daily_fee) - avg(daily_fee) * avg(discount_rate) / 100) * 30 < 2000000
order by 3 desc, 2, 1 desc



