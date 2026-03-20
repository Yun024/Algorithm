/* https://solvesql.com/problems/flow-and-stock/ */

select
  extract(year from acquisition_date) as "Acquisition year",
  count(1) as "New acquisitions this year (Flow)",
  sum(count(1)) over(order by extract(year from acquisition_date)) as "Total collection size (Stock)"
from artworks
where acquisition_date is not null
group by "Acquisition year"
order by "Acquisition year"