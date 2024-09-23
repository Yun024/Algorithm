-- 코드를 작성해주세요

# -------- join문 사용
# select 
#   b.year, 
#   max_year - a.size_of_colony as year_dev,  
#   id
# from ecoli_data a, 
#   (select year(differentiation_date) year, max(size_of_colony) max_year
#    from ecoli_data
#    group by year) b
# where year(a.differentiation_date) = b.year
# order by b.year, year_dev

#-------- correlated subquery 사용
# select year(differentiation_date) year, 
# (select max(size_of_colony) from ecoli_data where year(differentiation_date) = year) - size_of_colony as year_dev, id
# from ecoli_data
# order by year, year_dev


# -------- with문 사용
with max_colony as (
select max(size_of_colony) max_col, year(differentiation_date) year
from ecoli_data group by year)

select m.year, max_col - size_of_colony as year_dev, id
from ecoli_data a, max_colony m
where year(a.differentiation_date) = m.year
order by year, year_dev

# -------- 윈도우 함수 사용
# select 
# year(differentiation_date) year, 
# max(size_of_colony) over(partition by year(differentiation_date)) - size_of_colony as year_dev, id
# from ecoli_data
# order by year, year_dev