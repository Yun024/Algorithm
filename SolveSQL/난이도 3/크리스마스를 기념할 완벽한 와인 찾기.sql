-- /* https://solvesql.com/problems/wines-for-friends/ *

with avg_table as(
  select 
    avg(density) avg_density,
    avg(residual_sugar) avg_sugar,
    avg(case when color='white' then pH end) avg_pH,
    avg(case when color='white' then citric_acid end) avg_acid
  from wines
)

select w.*
from wines w
cross join avg_table a
where w.color = 'white'
and w.quality >= 7 
and w.density > a.avg_density
and w.residual_sugar > a.avg_sugar
and w.pH < a.avg_pH
and w.citric_acid > a.avg_acid;