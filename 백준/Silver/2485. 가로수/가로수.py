import sys
input = sys.stdin.readline
a = int(input().strip())
num_list = [int(input().strip()) for i in range(a)]
set_minus = set()
for i in range(len(num_list)-1):
    set_minus.add(num_list[i+1] - num_list[i])
list_minus = list(set_minus)
while len(list_minus) != 1:
    a,b = list_minus.pop(), list_minus.pop()
    while b != 0:
        a,b = b, a%b
    list_minus.append(a)
print(len(range(num_list[0],num_list[-1]+1,list_minus[0])) - len(num_list))