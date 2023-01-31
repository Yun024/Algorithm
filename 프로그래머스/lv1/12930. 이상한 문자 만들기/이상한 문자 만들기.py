# def solution(s):
#     final =[]
#     for i in s.split(" "):
#         answer = ""
#         for j,e in enumerate(i):
#             if j%2 == 0:
#                 answer += e.upper()
#             else:
#                 answer += e.lower()
#         final.append(answer)
#     return ' '.join(final)
def solution(s):
    return ' '.join([''.join([e.upper() if j%2 ==0 else e.lower() for j,e in enumerate(i)]) for i in s.split(" ")])
