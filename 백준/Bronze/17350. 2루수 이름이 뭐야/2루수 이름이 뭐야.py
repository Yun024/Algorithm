import sys
input = sys.stdin.readline

n = int(input().strip())
for _ in range(n):
    strings = input().strip()
    if strings == "anj":
        print("뭐야;")
        break
else:
    print("뭐야?")

