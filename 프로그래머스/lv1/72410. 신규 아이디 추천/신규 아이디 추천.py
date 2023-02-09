
def solution(new_id):
    # 정규식을 활용한 풀이
    import re
    new_id = new_id.lower()
    new_id = re.sub("[^0-9a-z._-]","",new_id)
    new_id = re.sub("\.+",".",new_id)
    new_id = re.sub("^[.]|[.]$","",new_id)
    new_id = "a" if len(new_id)==0 else new_id[:15]
    new_id = re.sub("[.]$","",new_id)
    new_id = new_id.ljust(3,new_id[-1])
    return new_id
    
#     최초 풀이
#     from string import ascii_lowercase
#     possible = [i for i in ascii_lowercase] + list(map(str,range(10))) + ["-","_","."]
#     new_id = new_id.lower()
#     new_id = [i for i in new_id if i in possible]
#     ans = new_id[0]
#     for i in new_id[1:]:
#         if i=="." and ans[-1] != ".":
#             ans+=i
#         elif i !="." :
#             ans +=i
#     new_id = ans.strip(".")
#     new_id = "a" if len(new_id)==0 else new_id
#     new_id = new_id[:15].strip(".")
#     if len(new_id)<3:
#         while len(new_id)!=3:
#             new_id += new_id[-1]
#     return new_id
    
    