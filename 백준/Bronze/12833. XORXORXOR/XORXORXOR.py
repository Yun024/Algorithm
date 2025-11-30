import sys
s1,s2,s3 = map(int,sys.stdin.readline().split())

print(s1^s2 if s3%2 else s1)