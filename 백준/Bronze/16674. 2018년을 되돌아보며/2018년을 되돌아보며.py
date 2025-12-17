import sys
from collections import Counter

strings = sys.stdin.readline().strip()
goal = set(['0','1','2','8'])
num_cnt = Counter(strings).most_common()
if set(strings) & goal == set(strings):
    if set(strings) & goal == goal:
        if num_cnt[0][1] == num_cnt[3][1]:
            print(8)
        else:
            print(2)
    else:
        print(1)
else:
    print(0)