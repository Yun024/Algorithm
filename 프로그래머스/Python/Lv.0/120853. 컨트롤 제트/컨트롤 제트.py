def solution(s):
    answer = 0
    for i in range(len(s.split(" "))):
        if s.split(" ")[i] != "Z":
            answer += int(s.split(" ")[i])
        elif s.split(" ")[i]=="Z":
            answer -= int(s.split(" ")[i-1])
    return answer