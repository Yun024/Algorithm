import re
def solution(s):
    word = {"zero":"0",
            "one":"1",
            "two":"2",
            "three":"3",
            "four":"4",
            "five":"5",
            "six":"6",
            "seven":"7",
            "eight":"8",
            "nine":"9"}
    s_str = re.sub(r"[^a-z]","",s)
    str_list = [i for i in list(word.keys()) if i in s_str]
    for i in str_list:
        s = s.replace(i,word[i])
    return int(s)

# def solution(s):
#     word = {"zero":"0",
#             "one":"1",
#             "two":"2",
#             "three":"3",
#             "four":"4",
#             "five":"5",
#             "six":"6",
#             "seven":"7",
#             "eight":"8",
#             "nine":"9"}
#     for i in [i for i in list(word.keys()) if i in re.sub(r"[^a-z]","",s)]:
#         s = s.replace(i,word[i])
#     return int(s)