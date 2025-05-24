import sys
input = sys.stdin.readline

n,m = map(int,input().split())

def cutting(m):

    tree = list(map(int,input().split()))
    start = 1
    end = max(tree) -1
    result = 0

    while start <= end:
        
        mid = (start + end) // 2
        total = sum(i - mid for i in tree if i > mid)

        if total >= m:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result

print(cutting(m))