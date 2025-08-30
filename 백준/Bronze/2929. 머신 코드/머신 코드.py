import sys

old = sys.stdin.readline().strip()
cnt, idx = 0,0
for s in old:
    if s.isupper() and idx%4:
        cnt += 4 - idx%4
        idx += 4 - idx%4
    idx += 1

print(cnt)
        
    
