# -- 코드를 작성해주세요

# 2진수를 이용한 문제풀이
# conv(genotype,10,2)를 통해 확인


select count(*) count
from ecoli_data
where not(genotype & 2) and genotype & 5

# select *, lpad(conv(genotype,10,2),4,0)
# from ecoli_data