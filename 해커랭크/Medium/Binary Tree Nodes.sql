## Url : https://www.hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true

with recursive node as (
select N,P,1 as c
from bst
where P is null
union all
select a.N,a.P,c+1
from bst a, node b
where a.P= b.N
)

select N,
case when c = 1 then 'Root'
when c = (select max(c) from node) then 'Leaf'
else 'Inner'
end as ccc 
from node
order by N