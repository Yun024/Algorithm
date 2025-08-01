import sys
input = sys.stdin.readline

last = []
for i,v in zip(range(1,7),[500,300,200,50,30,10]):
    for _ in range(i):
        last.append(v)
last.append(0)

this = []
for i in range(1,6):
    for _ in range(2**(i-1)):
        this.append(2**(10-i))
this.append(0)

t = int(input().strip())
for _ in range(t):
    ans = 0
    one,two = list(map(lambda x: int(x)-1,input().split()))
    ans += last[min(21,one)]
    ans += this[min(31,two)]
    print(ans*10000)