def braket(ss):
    stack = []
    brakets = {
        "]":"[",
        "}":"{",
        ")":"("}
    for i in ss:
        if not stack:
            if brakets.get(i):
                return 0 
            else:
                stack.append(i)
        elif brakets.get(i) == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    if not stack:
        return 1
    else:
        return 0 
            

def solution(s):
    ln = len(s)
    s *= 2
    ans = 0
    for i in range(ln):
        ans += braket(s[i:i+ln])
    return ans