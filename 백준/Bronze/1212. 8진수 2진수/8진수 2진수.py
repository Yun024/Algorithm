import sys
input = sys.stdin.readline

number = input().strip()
print(bin(int(number,8))[2:])