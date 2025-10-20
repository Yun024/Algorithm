import sys
input = sys.stdin.readline

n = int(input().strip())
strings = input().strip()
A_count = strings.count("A")
B_count = strings.count("B")
if A_count > B_count:
    print("A")
elif A_count < B_count:
    print("B")
else:
    print("Tie")