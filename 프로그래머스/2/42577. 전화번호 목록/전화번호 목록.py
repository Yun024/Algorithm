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

# def solution(pb):
#     pb.sort()
#     for i in range(len(pb)-1):
#         if pb[i] == pb[i+1][:len(pb[i])]:
#             return False
#     return True



def solution(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False
    return True

# def solution(pb):
#     ans = []
#     for i in pb:
#         ans.append(i)
#     for p in pb:
#         temp=""
#         for n in p:
#             temp += n
#             if temp in ans and temp != p:
#                 return False
#     return True