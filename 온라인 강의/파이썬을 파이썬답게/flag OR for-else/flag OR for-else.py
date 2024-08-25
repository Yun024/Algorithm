## 나의 풀이
# ans = [] 
# ans.append(int(input()))
# for i in range(4):
#     ans.append(int(input()) * ans[i])
# answer = [i for i in ans if i**0.5 == int(i**0.5)]
# print('found' if len(answer)!=0 else 'not found')

## 주어진 풀이(math사용)
import math
ans = [int(input()) for i in range(5)]
key = 1
answer = []
for i in ans:
    key *= i
    if math.sqrt(key) == int(math.sqrt(key)):
        answer.append(key)
print('found' if len(answer) !=0 else 'not found') 