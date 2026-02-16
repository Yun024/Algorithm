## Url: https://solvesql.com/problems/good-days-for-a-seoulforest-picnic/

select measured_at as good_day
from measurements
where to_char(measured_at,'YYYY-MM') = '2022-12'
  and pm2_5 <= 9
;