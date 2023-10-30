def solution(arr):
    i = 0
    stk = []
    while i < len(arr):
        if not stk:
            stk.append(arr[i])
            i +=1
        elif stk and stk[-1] == arr[i]:
            stk = stk[:max(len(stk)-1,0)]
            i +=1
        else: 
            stk.append(arr[i])
            i +=1
    return [-1] if not stk else stk
        