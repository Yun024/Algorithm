import sys
input = sys.stdin.readline

n = int(input().strip())
strings = input().strip()

hiarc = ['H','I','A','R','C']
print(min([strings.count(elem) for elem in hiarc]))   