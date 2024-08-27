-- 코드를 작성해주세요
select count(*) fish_count, max(ifnull(length,10)) max_length, fish_type
from fish_info 
group by fish_type
having avg(ifnull(length,10)) >= 33
order by fish_type