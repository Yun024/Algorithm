def solution(binomial):
    ans = [int(i) if j%2 ==0 else i for j,i in enumerate(binomial.split(' '))]
    if ans[1] == "+":
        return ans[0] + ans[2]
    elif ans[1] == '-':
        return ans[0] - ans[2]
    elif ans[1] == '*':
        return ans[0] * ans[2]
    elif ans[1] == '/':
        return ans[0] / ans[2]

    # eval(binomial)