
def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    answer = [[a[i%len(a)]==j,b[i%len(b)]==j,c[i%len(c)]==j] for i,j in enumerate(answers)]
    final = sum(sum(answer,[])[::3]),sum(sum(answer,[])[1::3]),sum(sum(answer,[])[2::3])
    return [j+1 for j,i in enumerate(final) if i==max(final)]