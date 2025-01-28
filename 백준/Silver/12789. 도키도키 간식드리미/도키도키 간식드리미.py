input()
num = list(map(int, input().split()))[::-1]
ans ,temp = [0], [0]
while num:
    if temp[-1] == ans[-1]+1:
        ans.append(temp.pop())
    elif ans[-1] +1 == num[-1]:
        ans.append(num.pop())
    else:
        temp.append(num.pop())
final = ans[1:] + temp[:0:-1]
print("Nice") if final == sorted(final) else print("Sad")