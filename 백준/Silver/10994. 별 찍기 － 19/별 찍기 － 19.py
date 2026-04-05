import sys

n = int(sys.stdin.readline().strip())
cnt = (n-1)*4+1
ans = [[' ']*cnt for i in range(cnt)]

for i in range(n):
    if not i:
        ans[cnt//2][cnt//2] = '*'
        continue

    elif i == n-1:
        for x in range(cnt):
            for y in range(cnt):
                if not x or x == cnt-1:
                    ans[x][y] = '*'
                elif not y or y == cnt-1:
                    ans[x][y] = '*'
    
    else:
        left,right = 2*i,cnt-(2*i)
        for x in range(left,right):
            for y in range(left,right):
                if x == left or x == right-1:
                    ans[x][y] = '*'
                elif y == left or y == right-1:
                    ans[x][y] = '*'

for i in ans:
    print(''.join(i))