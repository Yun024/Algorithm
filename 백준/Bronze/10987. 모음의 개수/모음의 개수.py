import sys
input = sys.stdin.readline

strings = input().strip()
res = sum([strings.count(i) for i in ['a','e','i','o','u']])
print(res)