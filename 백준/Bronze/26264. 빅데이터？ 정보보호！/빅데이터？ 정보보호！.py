import sys
input = sys.stdin.readline

n = int(input().strip())
strings = input().strip()

s_cnt = strings.count("security")
b_cnt = strings.count("bigdata")

if s_cnt > b_cnt:
    print("security!")
elif s_cnt == b_cnt:
    print("bigdata? security!")
else:
    print("bigdata?")