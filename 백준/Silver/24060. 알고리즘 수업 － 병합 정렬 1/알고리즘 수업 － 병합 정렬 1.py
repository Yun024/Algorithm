def merge_sort(A, p, r, cnt):
    if p < r:
        q = (p + r) // 2  # 중간 지점 계산
        cnt = merge_sort(A, p, q, cnt)      # 전반부 정렬
        cnt = merge_sort(A, q + 1, r, cnt)  # 후반부 정렬
        cnt = merge(A, p, q, r, cnt)        # 병합
    return cnt

def merge(A, p, q, r,cnt):
    i, j, t = p, q + 1, 0
    global b, ans
    tmp = [0] * (r - p + 1)  # 임시 배열 생성
    
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            i += 1
        else:
            tmp[t] = A[j]
            j += 1
        t += 1
    
    while i <= q:  # 왼쪽 배열의 남은 요소 복사
        tmp[t] = A[i]
        i += 1
        t += 1
    
    while j <= r:  # 오른쪽 배열의 남은 요소 복사
        tmp[t] = A[j]
        j += 1
        t += 1
    
    # 병합된 배열을 원본 배열 A에 반영
    for k in range(len(tmp)):
        A[p + k] = tmp[k]
        cnt +=1
        if cnt == b:
            ans = tmp[k]
    return cnt

a, b = map(int,input().split())
A = list(map(int,input().split()))
cnt = 0
ans = None
merge_sort(A,0,len(A)-1,cnt)
print(ans) if ans else print(-1)
