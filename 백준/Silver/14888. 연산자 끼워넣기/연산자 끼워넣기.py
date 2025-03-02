import sys
from collections import deque
input = sys.stdin.readline

input()
nums = list(map(int,input().split()))
ans = nums[0]
nums = nums[1:]
oper = list(map(int,input().split()))
queue = deque([(ans,nums,oper)])
max_v, min_v = -1000000000, 1000000000
answer = []
while queue:
    ans, nums, oper = queue.popleft()
    if nums:
        num = nums[0]
        temp_nums = nums[1:]
        for j,i in enumerate(oper):
            if i != 0:
                if j == 0:
                    queue.append((ans+num,temp_nums,[oper[0]-1,oper[1],oper[2],oper[3]]))
                elif j == 1:
                    queue.append((ans-num,temp_nums,[oper[0],oper[1]-1,oper[2],oper[3]]))
                elif j == 2:
                    queue.append((ans*num,temp_nums,[oper[0],oper[1],oper[2]-1,oper[3]]))
                else:
                    if ans > 0:
                        queue.append((ans//num,temp_nums,[oper[0],oper[1],oper[2],oper[3]-1]))
                    else:
                        queue.append((abs(ans) // num * -1,temp_nums,[oper[0],oper[1],oper[2],oper[3]-1]))
    else:
        max_v = max(max_v,ans)
        min_v = min(min_v,ans)

print(max_v)
print(min_v)
