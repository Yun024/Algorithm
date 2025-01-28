import sys
str_list = list(map(lambda x: x.strip(),sys.stdin.readlines()))[:-1]
dic ={
        "]":"[",
        ")":"("
    }
for i in str_list:
    stack = []
    for j in i[:-1].replace(" ",""):
        if not j.isalpha():
            if stack and stack[-1] == dic.get(j):
                stack.pop()
            else:
                stack.append(j)
    print("no") if stack else print("yes")