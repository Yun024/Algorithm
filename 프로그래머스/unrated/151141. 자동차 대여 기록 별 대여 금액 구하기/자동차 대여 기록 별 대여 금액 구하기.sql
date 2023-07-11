select history_id, max(fee) fee
from(
select history_id,
case 
when to_number(end_date - start_date) +1 < 7 then daily_fee * (to_number(end_date - start_date)+1)
when to_number(end_date - start_date) +1 >= 7 and to_number(end_date - start_date) +1 < 30 then (daily_fee - daily_fee * 5 /100 ) * (to_number(end_date - start_date)+1)
when to_number(end_date - start_date) +1 >= 30 and to_number(end_date - start_date) +1 < 90 then (daily_fee - daily_fee * 8 /100 ) * (to_number(end_date - start_date) +1)
else (daily_fee - daily_fee * 15 /100 ) * (to_number(end_date - start_date) +1)
end as fee 
from car_rental_company_car a, car_rental_company_rental_history b, car_rental_company_discount_plan c 
where a.car_id = b.car_id
and a.car_type = c.car_type
and a.car_type = '트럭'
) group by history_id
order by fee desc, history_id desc
