from collections import deque
def solution(p):
    
    def bracket_reverse(p):
        temp = p[1:-1]
        result = ""
        for i in temp:
            if i =="(":
                result += ")"
            else:
                result += "("
        return result
    
    def uv_split(p):
        l,r = 0,0
        for i in range(len(p)):
            if p[i] == "(":
                l += 1
            else:
                r += 1
            if l == r:
                break
        u,v = p[:i+1],p[i+1:]
        return u,v
    
    def is_right(p):
        q = deque(p)
        stack = []
        while q:
            bracket = q.popleft()
            if bracket == "(":
                stack.append(bracket)
            else:
                try:
                    stack.pop()
                except:
                    return False
        return True
    
    if not p:
        return p
    u,v = uv_split(p)
    if is_right(u):
        return u + solution(v)
    else:
        return "(" + solution(v) + ")" + bracket_reverse(u)
