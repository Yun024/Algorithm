def solution(babbling):
    possible = ["aya","ye","woo","ma"]
    answer = []
    for i in babbling:
        for j in possible:
            if j*2 not in i:
                i = i.replace(j," ")
        answer.append(i)
    return len([i for i in answer if len(i.strip())==0])

# 첫번째 풀이
# def solution(babbling):
#     Non = ["ayaaya","yeye","woowoo","mama"]
#     possible = ["aya","ye","woo","ma"]
#     answer = []
#     for i in babbling:
#         if Non[0] in i:
#             pass
#         elif Non[1] in i:
#             pass
#         elif Non[2] in i:
#             pass
#         elif Non[3] in i:
#             pass
#         else:
#             for j in possible:
#                 i = i.replace(j," ")
#         answer.append(i)
#     return len([i.replace(" ","") for i in answer if len(i.replace(" ",""))==0])