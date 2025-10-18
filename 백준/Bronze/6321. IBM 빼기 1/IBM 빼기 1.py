import sys
input = sys.stdin.readline

t = int(input().strip())
res = []
for num in range(t):
    strings = input().strip()
    ans = ''.join([chr(ord(s)+1) if s != "Z" else "A" for s in strings])
    res.append(f"String #{num+1}\n{ans}")
print('\n\n'.join(res))