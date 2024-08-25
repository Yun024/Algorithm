-- 코드를 작성해주세요
# select count(*) fish_count
# from fish_info
# where substring(time,1,4) = 2021

select count(*) fish_count
from fish_info
where date_format(time,'%Y') = 2021