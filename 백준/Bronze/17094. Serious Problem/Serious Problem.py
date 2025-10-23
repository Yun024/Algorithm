import sys
input = sys.stdin.readline

length = int(input().strip())
strings = input().strip()
count_2 = strings.count("2")
count_e = strings.count("e")

if count_2 == count_e:
    print("yee")
elif count_2 > count_e:
    print("2")
else:
    print("e")