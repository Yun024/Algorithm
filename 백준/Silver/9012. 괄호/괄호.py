import sys
input = sys.stdin.readline
for i in range(int(input().strip())):
    ps = input().strip()
    stack = []
    for j in ps:
        if stack and stack[-1]=="(" and j ==")":
            stack.pop()
        else:
            stack.append(j)
    print("NO") if stack else print("YES")