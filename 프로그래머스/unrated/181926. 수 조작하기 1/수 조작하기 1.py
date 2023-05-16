def solution(n, control):
    dic = {"w":1,"s":-1,"d":10,"a":-10}
    for  i in control:
        n += dic[i]
    return n