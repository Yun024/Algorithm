import sys,re
input = sys.stdin.readline

num = 1
while 1:
    t = int(input().strip())
    if not t:
        break
    ans = [0,0,0]
    for _ in range(t):
        temp = list(map(int,re.findall("[0-9]+",input().strip())))
        if len(temp) == 1:
            ans[0] += temp[0]
        elif len(temp) == 2:
            if not sum(ans[1:3]):
                ans[1] = temp[0]
                ans[2] = temp[1]
            else:
                top = ans[1]*temp[1] + ans[2]*temp[0]
                bottom = ans[2]*temp[1]
                ans[0] += top//bottom
                ans[1] = top%bottom
                ans[2] = bottom
        else:
            ans[0] += temp[0]
            if not sum(ans[1:3]):
                ans[1] = temp[1]
                ans[2] = temp[2]
            else:
                top = ans[1]*temp[2] + ans[2]*temp[1]
                bottom = ans[2]*temp[2]
                ans[0] += top//bottom
                ans[1] = top%bottom
                ans[2] = bottom
    
    top,bottom = ans[1],ans[2]
    while bottom:
        top,bottom = bottom, top%bottom
    if top != 1:
        ans[1] //= top
        ans[2] //= top
        
    if not ans[1]:
        print(f"Test {num}: {ans[0]}")
    elif not ans[0]:
        print(f"Test {num}: {ans[1]}/{ans[2]}")
    else:
        print(f"Test {num}: {ans[0]},{ans[1]}/{ans[2]}")
    num += 1