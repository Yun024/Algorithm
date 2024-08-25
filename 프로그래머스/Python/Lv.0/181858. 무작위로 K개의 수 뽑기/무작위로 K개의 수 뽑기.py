def solution(arr, k):
    
    ans = []
    for i in arr:
        if len(ans) <k :
            if i not in ans:
                ans.append(i)
                
    return ans + (k - len(ans)) * [-1] if len(ans) < k else ans