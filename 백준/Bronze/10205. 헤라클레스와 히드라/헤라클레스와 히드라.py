import sys
input = sys.stdin.readline

t = int(input().strip())
ans = []
for num in range(t):

    head = int(input().strip())
    strings = input().strip()

    for s in strings:
        if head <= 0:
            break
        head -= 1
        if s == "c":
            head += 2
    
    ans.append(f"Data Set {num+1}:\n{head}")

print('\n\n'.join(ans))