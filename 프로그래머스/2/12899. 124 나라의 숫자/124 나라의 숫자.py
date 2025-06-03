
def solution(n):
    
    num = n
    
    cnt = 1
    while n > 3**cnt:
        
        n -= 3**cnt
        cnt +=1
    
    lng = ["1","2","4"]
    ans = ""
        
    for i in range(cnt-1,0,-1):

        index = n // 3**(i)
        ans += str(index)
        n -= index * 3**i
        
    if n == 0:
        return solution(num-1)[:-1] + "4"
    
    return ans.replace("2","4").replace("1","2").replace("0","1") + lng[n-1]
    
    
   