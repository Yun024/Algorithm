def solution(code):
    answer = ""
    mode = 0
    for j,i in enumerate(code):
        if mode:
            if i == "1":
                mode +=1
            else:
                if j%2 ==1 :
                    answer+= i
        else:
            if i=="1":
                mode -=1 
            else:
                if j%2 ==0:
                    answer +=i
    return answer if answer else "EMPTY"