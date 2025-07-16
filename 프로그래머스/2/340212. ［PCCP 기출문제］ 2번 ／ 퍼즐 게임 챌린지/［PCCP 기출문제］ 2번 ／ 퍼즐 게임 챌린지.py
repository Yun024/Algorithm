def solution(diffs, times, limit):
    
    start,end = 1,100000
    while start < end:
        mid = (start + end)//2
        ans = 0

        for i in range(len(diffs)):
            if diffs[i] <= mid:
                ans += times[i]
            else:
                ans += (times[i] + times[i-1]) * (diffs[i] - mid) + times[i]
        if ans <= limit:
            end = mid
        else:
            start = mid+1
    return end
            