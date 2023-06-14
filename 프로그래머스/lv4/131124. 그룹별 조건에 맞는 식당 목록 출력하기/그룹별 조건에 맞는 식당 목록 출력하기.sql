-- 코드를 입력하세요
## having을 이용한 정답 출력
select member_name, review_text, to_char(review_date,'YYYY-MM-DD') review_date
from member_profile A, rest_review B
where A.member_id = B.member_id
and a.member_id in      (select member_id
                         from rest_review
                         group by member_id
                         having count(*) =  (select max(count(member_id))
                                             from rest_review
                                             group by member_id)) 
order by review_date, review_text

----
## Rank() 함수를 이용한 정답 출력
select member_name, review_text, to_char(review_date,'YYYY-MM-DD') review_date
from member_profile A, rest_review B
where A.member_id = B.member_id
and a.member_id in (select member_id
                    from (
                        select member_id , rank() over(order by count(*) desc) rnk
                        from rest_review
                        group by member_id) 
                    where rnk =1 )
order by review_date, review_text
