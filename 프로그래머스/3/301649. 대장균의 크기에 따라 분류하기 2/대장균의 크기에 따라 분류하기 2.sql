-- 코드를 작성해주세요

## percent_rank 사용
with  percent_ecoli as 
(select id, percent_rank() over(order by size_of_colony desc) ps from ecoli_data)

select id,
case when ps <= 0.25 then 'CRITICAL'
when ps <= 0.50 then 'HIGH'
when ps <= 0.75 then 'MEDIUM'
else 'LOW'
end as colony_name
from
percent_ecoli
order by id

## ntile사용
# with ntile_ecoli as
# (select id, ntile(4) over(order by size_of_colony desc) nt_col from ecoli_data)

# select id,
# case when nt_col = 1 then 'CRITICAL' 
# when nt_col = 2 then 'HIGH' 
# when nt_col = 3 then 'MEDIUM' 
# else 'LOW'
# end as colony_name
# from ntile_ecoli
# order by id