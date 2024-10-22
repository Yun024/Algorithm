## Url : https://www.hackerrank.com/challenges/draw-the-triangle-1/problem?isFullScreen=true

with recursive star as
    (select 20 as n
    union all
    select n-1 from star where n >1 

)
select repeat('* ',n) from star
