import sys

docum = sys.stdin.read().replace("\n","")
ans = [0] * 26
for chra in docum:
    if chra != " ":
        ans[abs(97 - ord(chra))] += 1

max_val = max(ans)
res = ""
for idx,val in enumerate(ans):
    if val == max_val:
        res += chr(97+idx)
print(''.join(sorted(res)))