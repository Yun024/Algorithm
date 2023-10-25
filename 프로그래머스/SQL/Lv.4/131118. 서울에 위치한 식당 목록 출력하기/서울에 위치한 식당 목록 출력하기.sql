-- 코드를 입력하세요
SELECT max(a.rest_id) rest_id, rest_name,  max(food_type) food_type, max(favorites) favorites, max(address) address, round(avg(review_score),2) score
from rest_info a, rest_review b
where a.rest_id = b.rest_id
group by rest_name
having max(address) like '서울%'
order by score desc, favorites desc