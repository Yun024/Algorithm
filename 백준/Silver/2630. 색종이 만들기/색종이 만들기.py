import sys

n = int(sys.stdin.readline().strip())
color =  list(map(lambda x: x.split(),sys.stdin.read().split("\n")))

def recursive(color,n,rs=0,cs=0):

    if all(color[j][i]=='1' for j in range(cs,cs+n) for i in range(rs,rs+n)):
        return '1'
    elif all(color[j][i]=='0' for j in range(cs,cs+n) for i in range(rs,rs+n)):
        return '0'
    return recursive(color,n//2,rs,cs) + recursive(color,n//2,rs+n//2,cs) +\
    recursive(color,n//2,rs,cs+n//2) + recursive(color,n//2,rs+n//2,cs+n//2)

answer = recursive(color,n)
print(answer.count("0"))
print(answer.count("1"))