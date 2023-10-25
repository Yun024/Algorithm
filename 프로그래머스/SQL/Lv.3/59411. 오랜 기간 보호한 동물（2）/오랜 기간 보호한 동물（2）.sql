-- 코드를 입력하세요
select *
from
(
    SELECT A.animal_id, A.name
    from animal_ins A inner join animal_outs B
    on A.animal_id = B.animal_id
    order by B.datetime - A.datetime desc 
)
where rownum <=2



