import string
def solution(s, n):
    answer = ""
    for i in s:
        if i.isupper():
            answer += string.ascii_uppercase[string.ascii_uppercase.index(i)+n-26]
        elif i.islower():
            answer += string.ascii_lowercase[string.ascii_lowercase.index(i)+n-26]
        else:
            answer += i
    return answer