-- 코드를 입력하세요
SELECT car_id ,round(avg(datediff(end_date,start_date)+1),1) as average_duration
from car_rental_company_rental_history
group by car_id
having average_duration >= 7
order by average_duration desc, car_id desc




# 평균 대여기간 round((sum(abs(datediff(start_date,end_date)))/count(car_id))+1,1) as average_duration

# truncate(avg(datediff(end_date,start_date)+1),1) as average_duration
# truncate도 똑같이 소숫점 하나까지 남기긴 하는데 반올림한것이아니라서 정답이 아님