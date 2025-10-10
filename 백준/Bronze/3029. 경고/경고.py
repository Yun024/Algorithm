import sys
from datetime import datetime,timedelta
input = sys.stdin.readline

res = [input().strip() for _ in range(2)]

form = "%H:%M:%S"

before = datetime.strptime(res[0],form)
after = datetime.strptime(res[1],form)

ans = str(after + timedelta(days=1) - before) if before > after else \
"24:00:00" if before == after else str(after - before)
print("0"+ans if len(ans) == 7 else ans)