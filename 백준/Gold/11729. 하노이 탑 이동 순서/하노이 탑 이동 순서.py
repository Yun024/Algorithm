
def hanoi(n, start, main, sub):
    if n ==1:
        ans.append([f"{start} {main}"])
        return 
    hanoi(n-1, start, sub, main)
    ans.append([f"{start} {main}"])
    hanoi(n-1, sub, main, start)
    
n = int(input())
ans = []
hanoi(n, 1, 3, 2)
print(len(ans))
for i in ans:
    print(*i)