## Url : https://www.hackerrank.com/challenges/print-prime-numbers/problem?isFullScreen=true

with recursive number as(
select 1 as n 
union all
select n+1
from number
where n < 1000)

select group_concat(aa.n separator '&')
from number aa
inner join (select a.n from number a inner join number b on a.n mod b.n != 0 and a.n >= b.n or a.n =2 
            group by a.n having count(a.n) = a.n - 2 or a.n = 2) bb on aa.n = bb.n