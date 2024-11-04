## Url : https://www.hackerrank.com/challenges/full-score/problem?isFullScreen=true

select d.hacker_id, d.name
from submissions a
inner join challenges b on a.challenge_id = b.challenge_id
inner join difficulty c on b.difficulty_level = c.difficulty_level 
inner join hackers d on a.hacker_id = d.hacker_id
where c.score = a.score
group by d.hacker_id, d.name
having count(d.hacker_id) > 1
order by count(d.hacker_id) desc, d.hacker_id 