my_str = input().strip()

# for문 사용
# ans = [[i,len([j for j in my_str if i==j])] for i in set(my_str)]
# x = max([i[1] for i in ans])
# print(''.join(sorted(([i[0] for i in ans if i[1] == x]))))

# collections 사용
from collections import Counter
ans = Counter(my_str).most_common()
print(''.join(sorted([i[0] for i in ans if i[1] == ans[0][1]])))