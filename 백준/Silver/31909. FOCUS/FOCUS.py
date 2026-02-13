import sys
input = sys.stdin.readline

n = int(input().strip())
ans = list(range(0,8))
commands = list(map(int,input().split()))
stop = ans[int(input().strip())]


for command in commands:
    binary = bin(command)[2:]
    
    if binary.count('1') == 2:
        temp = []
        for i,v in enumerate(binary[::-1]):
            if v == '1':
                temp.append(i)
        a,b = temp[0],temp[1]
        ans[a],ans[b] = ans[b],ans[a]
        

print(ans[stop])    