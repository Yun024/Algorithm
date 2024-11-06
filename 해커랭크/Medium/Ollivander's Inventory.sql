## Url : https://www.hackerrank.com/challenges/harry-potter-and-wands/problem?isFullScreen=true

select a.id, b.age, a.coins_needed, a.power
from wands a 
inner join wands_property b on a.code = b.code 
inner join (select a.power, b.age, min(coins_needed) as coins_needed 
            from  wands a inner join wands_property b 
            on a.code = b.code
            where b.is_evil = 0 
            group by a.power, b.age) sub 
on a.power = sub.power and b.age = sub.age and a.coins_needed = sub.coins_needed
order by a.power desc, b.age desc