import sys
input = sys.stdin.readline


def is_stack():

    calcul = input().strip()
    num = ''
    stack = []

    for i in calcul:
        if i == "-" or i == "+":
            stack.append(int(num))
            num = ''
            stack.append(i)
        else:
            num += i
    stack.append(int(num))
    
    return stack[::-1]

stack = is_stack()
num = stack.pop()
status = '+'
minus_num = 0

while stack:

    item = stack.pop()
    if status == '+':
        if item == '-':
            status = '-'
        elif item != '+':
            num += item

    else:
        if item != '-' and item !='+':
            num -= item

print(num)