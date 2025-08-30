import sys
s = sys.stdin.readline().split()

ans = []
temp = ""
if '_' in s[1]:
    for ss in s[1]:
        if ss == "_":
            ans.append(temp)
            temp = ""
        else:
            temp += ss
else:
    for ss in s[1]:
        if ss.isupper():
            ans.append(temp)
            temp = ss
        else:
            temp += ss
ans.append(temp)

if int(s[0]) == 1:
    print(s[1])
    print('_'.join(ans).lower())
    print(ans[0][0].upper() + ans[0][1:] + ''.join(ans[1:]))
elif int(s[0]) == 2:
    ans = ''.join(list(map(lambda x:x[0].upper()+x[1:] ,ans)))
    print(ans[0].lower() + ans[1:])
    print(s[1])
    print(ans)
else:
    print(s[1][0].lower() + s[1][1:])
    print('_'.join(ans[1:]).lower())
    print(s[1])