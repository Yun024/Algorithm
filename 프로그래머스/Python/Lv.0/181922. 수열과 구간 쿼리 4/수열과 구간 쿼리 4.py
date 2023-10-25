def solution(arr, queries):
    for i in queries:
        ans = [j for j in list(range(i[0],i[1]+1)) if j%i[2]==0]
        for c in ans:
            arr[c] +=1
    return arr