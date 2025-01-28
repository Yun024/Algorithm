def solution(s):
    temp = s[1:-1].split("}")[:-1]
    temp2 = [i.split("{")[1:] for i in temp]
    temp3 = [i.split(",") for i in sum(temp2,[])]
    temp4 = [[int(j) for j in i] for i in temp3]
    temp5 = sorted(temp4, key=lambda x: len(x))
    ans = []
    for i in temp5:
        ans.append([j for j in i if j not in ans][0])
    return ans