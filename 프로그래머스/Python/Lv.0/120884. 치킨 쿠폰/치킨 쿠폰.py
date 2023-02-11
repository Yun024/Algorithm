def solution(chicken):
    coupon = 0
    unuse = 0
    while chicken >= 10:
        coupon += chicken//10
        unuse += chicken%10
        chicken = chicken//10
    if unuse%9 ==0:
        coupon += unuse/9
    return coupon