import sys
strings = sys.stdin.readline()

temp = set(strings)
ans = 0

for s in ['M','O','B','I','S']:
    if s in temp:
        ans +=1
    
print('YES' if ans == 5 else 'NO')