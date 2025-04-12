## Url : https://solvesql.com/problems/refine-cafe-address/

select 
  substr(address,1,instr(address,' ')-1) sido,
  substr(
    address,
    instr(address,' ')+1,
    instr(substr(address, instr(address,' ')+1),' ')-1
  ) sigungu,
  count(*) cnt
from cafes
group by sido, sigungu
order by cnt desc
