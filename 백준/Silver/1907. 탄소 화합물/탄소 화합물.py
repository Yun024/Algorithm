import sys,re

def multiply_list(lst,i):
    return [x*i for x in lst]

def trans(inpt):

    dic = {'C':0,'H':1,'O':2}
    res = [0]*3
    temp = inpt[0]

    if len(inpt) == 1:
        res[dic[temp]] += 1
        return res

    for i in range(1,len(inpt)):
        if inpt[i].isnumeric():
            res[dic[temp]] += 1*int(inpt[i])
            temp = ""
        else:
            if not temp:
                temp += inpt[i]
            else:
                res[dic[temp]] += 1
                temp = inpt[i]
    if temp:
        res[dic[temp]] += 1
    return res

def find_answer(a,b,c):
    for i in range(1,11):
        for j in range(1,11):
            for u in range(1,11):
                at,bt,ct = multiply_list(a,i), multiply_list(b,j), multiply_list(c,u)
                if [att+btt for att,btt in zip(at,bt)] == ct:
                    return [i,j,u]
                
    


strings = sys.stdin.readline().strip()

aa,bb,cc = re.findall("[0-9A-Z]+",strings)
a,b,c = trans(aa),trans(bb),trans(cc)
print(*find_answer(a,b,c))
