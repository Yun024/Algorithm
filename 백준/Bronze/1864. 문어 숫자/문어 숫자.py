import sys
input = sys.stdin.readline
oct_dic = {"-":0,"\\":1,"(":2,"@":3,"?":4,">":5,"&":6,"%":7,"/":-1}

while 1:
    strings = input().strip()
    if strings == "#":
        break
    ans = 0
    length = len(strings) - 1
    for idx,s in enumerate(strings):
        ans += oct_dic[s] * (8 ** (length - idx))
    print(ans)