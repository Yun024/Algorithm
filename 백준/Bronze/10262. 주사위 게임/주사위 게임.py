import sys
input = sys.stdin.readline

num1 = list(map(int,input().split()))
num2 = list(map(int,input().split()))

ans1 = sum(num1)
ans2 = sum(num2)

print("Gunnar" if ans1 > ans2 else "Emma" if ans1 < ans2 else "Tie")