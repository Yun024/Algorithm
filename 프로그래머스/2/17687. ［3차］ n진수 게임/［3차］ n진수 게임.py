def solution(n, t, m, p):
    dic = {"10":"A","11":"B","12":"C","13":"D","14":"E","15":"F"}
    def trans(i,n):
        if i == 0:
            return "0"
        ans = ""
        while i:
            ans += dic.get(str(i%n),str(i%n))
            i = i//n
        return ans[::-1]
    result = ""
    cnt = 0
    while len(result) <= t*m :
        result += trans(cnt,n)
        cnt +=1
    return result[p-1:t*m:m]