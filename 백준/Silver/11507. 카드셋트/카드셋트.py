import sys
from collections import defaultdict

strings = sys.stdin.readline().strip()
dic = defaultdict(list)
dic['P'], dic['K'], dic['H'], dic['T']
for i in range(0,len(strings),3):
    key,value = strings[i],strings[i+1:i+3]
    if int(value) in dic[key]:
        print("GRESKA")
        break
    dic[key].append(int(value))
else:
    print(*list(map(lambda x: 13-len(x),dic.values())))