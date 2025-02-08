def solution(numbers):
    ans = []
    stack = []
    for i in numbers[::-1]:
        while stack and i >= stack[-1]:
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
        stack.append(i)
    return ans[::-1]