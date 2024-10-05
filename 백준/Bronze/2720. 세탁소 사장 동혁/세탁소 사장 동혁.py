num = int(input())
change = [25,10,5,1]
answer = [0,0,0,0]
for i in range(num):
    cent = int(input())
    for u,k in enumerate(change):
        answer[u] = cent // k  
        cent = cent % k 
    print(*answer)