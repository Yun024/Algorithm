import sys,re
input = sys.stdin.readline

t = int(input().strip())
nums = []
for _ in range(t):
    strings = input().strip()
    temp =list(map(int,re.findall('[0-9]+',strings)))
    nums += temp

for n in sorted(nums):
    print(n)