def solution(id_pw, db):
    for i in db:
        if id_pw[0] == i[0] and id_pw[1] == i[1]:
            answer = "login"
            break
        elif id_pw[0] == i[0] and id_pw[1] != i[1]:
            answer = "wrong pw"
            break
        else : 
            answer = "fail"
    return answer