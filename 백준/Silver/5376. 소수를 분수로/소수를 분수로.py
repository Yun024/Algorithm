import sys,re
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    strings = input().strip()
    temp = re.findall('[0-9]+',strings)
    if '(' in strings:
        if len(temp) == 2:
            a = int(temp[1]) 
            b = 10**len(temp[1]) - 1
        else:
            a = int(temp[1] + temp[2]) - int(temp[1])
            b = 10**(len(temp[1])+len(temp[2])) - 10**len(temp[1])
    else:
        length = len(temp[1])+1
        a,b = int(temp[1]), int('1'.ljust(length,'0'))
    
    t1,t2 = b,a
    while t2:
        t1,t2 = t2,t1%t2
    print(a//t1 ,'/', b//t1,sep='')