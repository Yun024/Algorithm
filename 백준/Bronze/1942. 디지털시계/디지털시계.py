import sys
from datetime import datetime,timedelta
input = sys.stdin.readline
form = "%H:%M:%S"

for _ in range(3):
    a,b = input().split()
    aa,bb = datetime.strptime(a,form), datetime.strptime(b,form)
    temp = int((bb-aa+timedelta(days=1) if aa > bb else bb-aa).total_seconds())
    ans = 0
    for i in range(temp+1):
        cc = int((aa + timedelta(seconds=i)).strftime(form).replace(":",""))
        if not cc%3:
            ans += 1
    print(ans)