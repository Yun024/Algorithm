n = int(input())
ans = set()
for one in range(0,n+1):
    for two in range(n-one,-1,-1):
        for three in range(n-one-two,-1,-1):
            four = n-one-two-three
            ans.add(one*1 + two*5 + three*10 + four*50)
print(len(ans))