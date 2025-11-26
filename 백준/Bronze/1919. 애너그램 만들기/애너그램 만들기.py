import sys
input = sys.stdin.readline

first = input().strip()
second = input().strip()

fir_res = [0]*26
sec_res = [0]*26

for f in first:
    fir_res[ord(f)-97] += 1
for s in second:
    sec_res[ord(s)-97] += 1

ans = 0
for fr,sr in zip(fir_res,sec_res):
    ans += abs(fr-sr)

print(ans)
