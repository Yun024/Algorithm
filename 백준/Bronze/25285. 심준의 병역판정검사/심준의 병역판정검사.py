import sys
input = sys.stdin.readline

n = int(input().strip())
for _ in range(n):
    height,weight = map(int,input().split())
    bmi = weight / (height ** 2 / 10000)
    if height < 141:
        print(6)
    elif height < 146:
        print(5)
    elif height < 159:
        print(4)
    elif height < 161:
        if 16 <= bmi < 35:
            print(3)
        else:
            print(4)
    else:
        if 20 <= bmi < 25:
            print(1)
        elif 18.5 <= bmi < 20 or 25 <= bmi < 30:
            print(2)
        elif 16 <= bmi < 18.5 or 30 <= bmi < 35:
            print(3)
        else:
            print(4)