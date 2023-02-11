-- 코드를 입력하세요
SELECT 
    floor(price/10000)*10000 as price_group, count(*) as products
from product
group by price_group
order by price_group



# truncate(A,B) A는 숫자가 들어가고 
# B가 0일시 정수 출력 ,B가 양수일시 소수점 B자리까지, B가 음수일시 (10**B)/10의자리까지 0으로 출력 
# truncate(price,-4) => 만의 자리빼고 모두 0이됨
# truncate(price/10000,0)*10000 => 소수점 아래 제거
# floor(price/10000)*10000