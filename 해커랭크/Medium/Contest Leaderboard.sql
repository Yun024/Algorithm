## Url : https://www.hackerrank.com/challenges/contest-leaderboard/problem?isFullScreen=true

select a.hacker_id, max(b.name), sum(a.score)
from (
select hacker_id, challenge_id, max(score) score
from submissions 
group by hacker_id, challenge_id) a
inner join hackers b on a.hacker_id = b.hacker_id
group by a.hacker_id
having sum(a.score) != 0
order by sum(a.score) desc, a.hacker_id 