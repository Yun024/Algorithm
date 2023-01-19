select HISTORY_ID,CAR_ID,date_format(START_DATE,"%Y-%m-%d") START_DATE,date_format(END_DATE,"%Y-%m-%d") END_DATE, if (abs(start_date - end_date)>98,"장기 대여","단기 대여") RENT_TYPE
from car_rental_company_rental_history
where date_format(start_date,"%m")=09
order by history_id desc