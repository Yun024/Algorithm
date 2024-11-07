## Url : https://www.hackerrank.com/challenges/challenges/problem?isFullScreen=true

with cnt_chl as 
    (select hacker_id, count(challenge_id) cnt
    from challenges
    group by hacker_id)

select a.hacker_id, b.name, sub.cnt
from cnt_chl a
inner join hackers b on a.hacker_id = b.hacker_id
inner join (
        select cnt
        from cnt_chl
        group by cnt
        having count(cnt) = 1 or cnt = (select max(cnt) from cnt_chl)) as sub
        on a.cnt = sub.cnt
order by sub.cnt desc, a.hacker_id 