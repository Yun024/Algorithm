-- 코드를 입력하세요

## where절 서브쿼리(중첩서브쿼리) 사용 * in을 이용한 다중열 
select food_type,rest_id,rest_name,favorites
from rest_info
where (food_type,favorites) in
(
    select food_type,max(favorites)
    from rest_info
    group by food_type
)
order by food_type desc

## over함수, partition by, rank 함수 사용 
select food_type, rest_id, rest_name, favorites
from 
(
    select food_type, rest_id,rest_name, favorites,
    rank() over(partition by food_type order by favorites desc) as rk
    from REST_INFO
)
where rk = 1
order by food_type desc

