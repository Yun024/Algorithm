import sys
input = sys.stdin.readline

n,m = map(int,input().split())
ans,cnt,res = 0,0,[]

for _ in range(m):
	a,b = map(int,input().split())
	if a >= n:
		cnt += 1
	else:
		res.append(a)


if m-1 > cnt:
	res.sort()
	for _ in range(m-1-cnt):
		num = res.pop()
		ans += n-num

print(ans)
