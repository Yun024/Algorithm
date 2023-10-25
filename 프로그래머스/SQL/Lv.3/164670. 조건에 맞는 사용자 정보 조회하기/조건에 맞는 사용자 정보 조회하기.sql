-- 코드를 입력하세요
-- #서브쿼리 사용, 
select user_id,nickname, city||' '|| street_address1 || ' ' || street_address2 전체주소, 
regexp_replace(tlno,'(.{3})(.+)(.{4})','\1-\2-\3') 전화번호 
from used_goods_user U, 
(
select writer_id
from used_goods_board
group by writer_id
having count(writer_id) >=3 
) B
where U.user_id = B.writer_id
order by user_id desc

-- 서브쿼리대신 여러열에 대한 그룹바이 사용 
-- select user_id, nickname, city||' '|| street_address1||' '||street_address2 as 전체주소, regexp_replace(tlno,'(.{3})(.+)(.{4})','\1-\2-\3') as 전화번호
-- from used_goods_board B, used_goods_user U
-- where B.writer_id = U.user_id 
-- group by user_id,nickname, city, street_address1, street_address2, tlno
-- having count(user_id)>=3
-- order by user_id desc