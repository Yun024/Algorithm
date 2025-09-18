import sys,re
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
strings = input().strip()

def calcul(strings):

    oper = re.findall('[SMUPC]',strings)
    nums = deque([int(i) for i in re.findall('[0-9]+',strings)])
    temp = nums.popleft()
    ans = []
    for o in oper:
        if o == 'C':
            ans.append(temp)
        elif o == 'S' and nums:
            temp -= nums.popleft()
        elif o == 'P' and nums:
            temp +=  nums.popleft()
        elif o == 'M' and nums:
            temp *= nums.popleft()
        elif o == 'U' and nums:
            temp = int(temp / nums.popleft())

    return ans

res = calcul(strings)
print(*res) if res else print('NO OUTPUT')