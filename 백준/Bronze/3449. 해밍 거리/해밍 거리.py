import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    a,b = input().strip(), input().strip()
    ans = 0
    for i,j in zip(a,b):
        if i != j:
            ans +=1
    print(f"Hamming distance is {ans}.")
    