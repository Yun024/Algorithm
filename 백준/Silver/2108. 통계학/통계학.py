import sys
from collections import Counter

def most(num_list):
    counter = Counter(num_list).most_common()
    ans = [i[0] for i in counter if i[1] == counter[0][1]]
    return sorted(ans)[1] if len(ans)>1 else ans[0]

input()
num_list = sorted(map(int,sys.stdin.read().split()))
ln = len(num_list)

print(round(sum(num_list)/len(num_list)))
print(sum(num_list[ln//2-1:ln//2+1])//2) if ln%2 == 0 else print(num_list[ln//2])
print(most(num_list))
print(abs(num_list[0]-num_list[-1]))