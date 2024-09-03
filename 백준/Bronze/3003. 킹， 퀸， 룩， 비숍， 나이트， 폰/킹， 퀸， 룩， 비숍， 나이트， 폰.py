ans = [1,1,2,2,2,8]
a = map(int,input().split())
print(*[j-i for j,i in zip(ans,a)])