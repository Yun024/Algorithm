import heapq
def solution(operations):
    
    max_heap, min_heap = [],[]
    
    for operation in operations:
        order, num = operation.split()

        if order == "D" and max_heap: 
            if num == "1":
                temp = heapq.heappop(max_heap)
                min_heap.remove(-temp)
            else:
                temp = heapq.heappop(min_heap)
                max_heap.remove(-temp)
        elif order == "I":
            heapq.heappush(min_heap,int(num))
            heapq.heappush(max_heap,-int(num))
            
    return [-heapq.heappop(max_heap),heapq.heappop(min_heap)] if max_heap else [0,0]