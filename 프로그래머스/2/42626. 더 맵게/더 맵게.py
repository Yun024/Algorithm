
from heapq import *
def solution(scoville, K):
    heapify(scoville)
    cnt = 0
    while scoville[0] < K:
        a = heappop(scoville)
        if not scoville:
            return -1
        b = heappop(scoville)
        heappush(scoville,a + (b*2))
        cnt +=1
    return cnt