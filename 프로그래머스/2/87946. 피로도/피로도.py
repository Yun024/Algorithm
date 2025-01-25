# from itertools import permutations
# def solution(k, dungeons):
#     a = set()
#     for i in permutations(dungeons):
#         cnt = 0
#         fatigue = k
#         for m,n in i:
#             if fatigue >= m:
#                 fatigue -=n
#                 cnt +=1
#             else:
#                 break
#         a.add(cnt)
#     return max(a)
def dfs(k, dungeons, visited, count):
    global max_count
    max_count = max(max_count,count)
    
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k-dungeons[i][1], dungeons, visited, count+1)
            visited[i] = False


def solution(k, dungeons):
    global max_count
    max_count = 0
    visited = [False] * len(dungeons)
    dfs(k, dungeons, visited, 0)
    return max_count
    
    
    
    
    