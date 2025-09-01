import sys
from datetime import datetime

strings = sys.stdin.readline().strip()
strings = strings.replace(",","")
key = int(strings.split()[2])
now_time = datetime.strptime(strings,"%B %d %Y %H:%M")
next_time = datetime(key+1,1,1)
up = next_time - now_time
down = next_time - datetime(key,1,1) 
print((1 - up/down)*100)
