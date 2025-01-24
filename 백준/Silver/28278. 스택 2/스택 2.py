import sys
input()
cmd_list = list(map(lambda x: x.strip(), sys.stdin.readlines()))
stack = []
for i in cmd_list:
    if i[0] =='1':
        stack.append(int(i.split()[1]))
    if i[0] =='2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    if i[0] =='3':
        print(len(stack))
    if i[0] =='4':
        if stack:
            print(0)
        else:
            print(1)
    if i[0] =='5':
        if stack:
            print(stack[-1])
        else:
            print(-1)