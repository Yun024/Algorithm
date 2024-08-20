a = int(input())
b = str(input())
[print(a * int(i)) for i in b[::-1]]
print(a*int(b))