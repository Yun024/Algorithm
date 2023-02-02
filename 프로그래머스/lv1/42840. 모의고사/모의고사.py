
def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    a_ans,b_ans,c_ans = 0,0,0
    for i,j in enumerate(answers):
        a_ans+=(a[i%len(a)]==j)
        b_ans+=(b[i%len(b)]==j)
        c_ans+=(c[i%len(c)]==j)
    answer = [a_ans,b_ans,c_ans]
    #answer = [[a[i%len(a)]==j, b[i%len(b)]==j , c[i%len(c)]==j] for i,j in enumerate(answers)]
    #final = sum(sum(answer,[])[::3]),sum(sum(answer,[])[1::3]),sum(sum(answer,[])[2::3])
    return [j+1 for j,i in enumerate(answer) if i==max(answer)]