import sys
from datetime import datetime, timedelta
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    
    ym = input().strip()
    pars,frmt = "%Y %m", "%Y %m %d"
    
    diff_days = timedelta(days=1)
    ans_day = datetime.strptime(ym,pars) - diff_days
    ans = datetime.strftime(ans_day,frmt)
    print(*list(map(int,ans.split())))