a = int(input())
b,c = [],[]
for i in range(a):
    d,e = map(int,(input().split()))
    b.append(d)
    c.append(e)
print((max(b) - min(b)) * (max(c) - min(c)))