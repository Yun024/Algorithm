-- ## 서브쿼리 사용, having대신 where문 사용, 오라클 조인
-- select * 
-- from 
-- (
-- SELECT B.user_id, B.nickname, sum(price) total_sales
-- from used_goods_board A , used_goods_user B 
-- where A.writer_id = B.user_id and A.status = 'DONE'
-- group by B.user_id, B.nickname
-- )
-- where total_sales >= 700000
-- order by total_sales


-- 서브쿼리 사용x, having문 사용, 안시조인
select B.user_id, B.nickname, sum(A.price) total_sales
from used_goods_board A inner join used_goods_user B
on A.writer_id = B.user_id
where A.status = 'DONE'
group by B.user_id,B.nickname
having sum(A.price) >= 700000
order by total_sales