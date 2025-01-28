# def solution(pb):
#     pb.sort(key= lambda x: len(x))
#     l = 0
#     while l <= len(pb)-1:
#         r = len(pb)-1
#         while l != r:
#             if pb[r].startswith(pb[l]):
#                 return False
#             r -=1
#         l +=1
#     return True

def solution(pb):
    pb.sort()
    for i in range(len(pb)-1):
        if pb[i] == pb[i+1][:len(pb[i])]:
            return False
    return True
        