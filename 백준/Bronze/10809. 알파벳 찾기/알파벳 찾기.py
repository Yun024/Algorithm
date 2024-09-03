import string
a = string.ascii_lowercase
b = input()
print(*[b.find(i) for i in a])