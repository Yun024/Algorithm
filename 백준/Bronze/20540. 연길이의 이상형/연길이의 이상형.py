import sys

strings = sys.stdin.readline().strip()
dic = {"I":"E","E":"I","F":"T","T":"F","N":"S","S":"N","J":"P","P":"J"}

print(''.join([dic[s] for s in strings]))