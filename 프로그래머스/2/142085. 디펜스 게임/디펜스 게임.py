import heapq

def solution(n, k, enemy):
    
    if k >= len(enemy):
        return len(enemy)
    
    heap = []
    for i in range(k):
        heapq.heappush(heap,enemy[i])
        
    ans,num = k,0
    for _ in range(k,len(enemy)):
        heapq.heappush(heap,enemy[ans])
        num += heapq.heappop(heap)
        ans += 1
        if num > n:
            return ans-1
    return ans