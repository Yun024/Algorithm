import sys
input = sys.stdin.readline

def trans_s(strings):

    strings = ' '.join(strings.split())
    dic = {"{":"(" , "[":"(" , "}":")" , "]":")" , ";":"," , "(":"(" , ")":")" , ",":"," , ":":":" ,
        ".":"."}
    temp = ""

    for s in strings:
        if s in dic.keys():
            if temp and temp[-1] == " ":
                temp = temp[:-1] + dic[s]
            else:
                temp += dic[s]
        elif s == " " and temp[-1] in dic.keys():
            continue
        else:
            temp += s

    return temp
    
t = int(input().strip())
ans  = []

for n in range(t):
    s1 = input().strip().lower()
    s2 = input().strip().lower()
    if trans_s(s1) == trans_s(s2):
        ans.append(f"Data Set {n+1}: equal")
    else:
        ans.append(f"Data Set {n+1}: not equal")

print('\n\n'.join(ans))