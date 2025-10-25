import sys
input = sys.stdin.readline

n = int(input().strip())
strings = input().strip()
length = len(strings)

for i in range(length-1):
    if strings[i] == strings[i-1]:
        print("No")
        break
else:
    print("Yes")