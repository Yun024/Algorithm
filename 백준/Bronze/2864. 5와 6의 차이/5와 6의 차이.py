import sys

a,b = sys.stdin.readline().split()
max_val = int(a.replace("5","6")) + int(b.replace("5","6"))
min_val = int(a.replace("6","5")) + int(b.replace("6","5"))
print(min_val,max_val)