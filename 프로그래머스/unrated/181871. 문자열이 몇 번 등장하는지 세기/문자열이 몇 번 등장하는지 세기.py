def solution(myString, pat):
    answer = 0
    try:
        for i in range(len(myString)):
             if myString[i:i+len(pat)] == pat :
                    answer+=1 
    except :
        pass
    return answer