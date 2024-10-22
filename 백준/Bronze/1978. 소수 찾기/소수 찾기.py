int(input())
a = list(map(int,input().split()))

sum = 0
for i in a:
    if i != 1 :
        for j in range(2,i//2+1):
            if i%j == 0:
                sum-=1
                break
        sum +=1
print(sum)