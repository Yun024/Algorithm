a = int(input())
b = set()
for i in range(a):
    b.add(input())
c = sorted(b,key=lambda x: (len(x),x))
for i in c:
    print(i)