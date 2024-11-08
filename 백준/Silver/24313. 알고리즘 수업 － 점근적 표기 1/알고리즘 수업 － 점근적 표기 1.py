a1, a0 = map(int,input().split())
c = int(input())
n0 = int(input())

answer = 1
for n in range(n0,101):
    answer = answer * (a1 * n + a0 <= c * n)
print(answer)