import sys
en = int(sys.stdin.readline().strip())

ans = 0 
money = 1000 - en
for i in [500,100,50,10,5,1]:
    ans += money//i
    money %= i
print(ans)