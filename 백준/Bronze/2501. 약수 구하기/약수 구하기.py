a,b = map(int,input().split())
answer = 0
for i in range(1,a//2+1):
    if a%i == 0:
        answer+=1
    if answer == b:
        print(i)
        break
        
if answer+1==b :
    print(a)
elif answer+1 < b:
    print(0)