## Url : https://solvesql.com/problems/group-by/

select
  quartet,
  avg(x) x_mean,
  variance(x) x_var,
  round(avg(y), 2) y_mean,
  round(variance(y), 2) y_var
from
  points
group by
  quartet