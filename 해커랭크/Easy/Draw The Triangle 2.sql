## Url : https://www.hackerrank.com/challenges/draw-the-triangle-2/problem?isFullScreen=true

with recursive star as
    (select 1 as n 
    union all
    select n+1 from star where n<20)

select repeat('* ',n) from star