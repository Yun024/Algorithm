-- 코드를 작성해주세요

### 삼중조인
# select a.id, c.fish_name, a.length
# from fish_info a, 
# (select fish_type, max(length) mel
# from fish_info
# group by fish_type) b, 
# fish_name_info c
# where a.length = b.mel 
# and a.fish_type = b.fish_type
# and a.fish_type = c.fish_type
# order by id 

### dense rank사용
select a.id, b.fish_name, a.length 
from (
    select  fish_type, id,length,  dense_rank() over(partition by fish_type order by length desc) as rk
    from fish_info) a, fish_name_info b
where a.fish_type = b.fish_type
and a.rk = 1
order by a.id