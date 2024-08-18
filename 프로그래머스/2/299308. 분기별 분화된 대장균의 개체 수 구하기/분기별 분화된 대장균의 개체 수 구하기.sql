-- 코드를 작성해주세요
# select  quarter, count(id) ecoli_count from (
# select id,
# case when month(differentiation_date) < 4 then '1Q'
# when month(differentiation_date) >= 4 and month(differentiation_date) < 7 then '2Q'
# when month(differentiation_date) >= 7  and month(differentiation_date) < 10 then '3Q'
# when month(differentiation_date) >= 10 then '4Q'
# end as quarter
# from ecoli_data
# ) a group by quarter
# order by quarter
### ------------------ 처음풀이(무식하게)


# select 
# case when quarter(differentiation_date) = 1 then '1Q'
# when quarter(differentiation_date) = 2 then '2Q'
# when quarter(differentiation_date) = 3 then '3Q'
# else '4Q'
# end as quarter, count(id) ecoli_count
# from ecoli_data
# group by quarter
# order by quarter
# ;
### ------------------- casewhen을 쓰되 보기쉽게

select 
concat(ceil(month(differentiation_date)/3),'Q') quarter, count(id) ecoli_count
from ecoli_data
group by quarter
order by quarter
;
### -------------------- casewhen을 쓰지 않고 공식을 통해 분기 계산