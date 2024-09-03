a = input().upper()
b = sorted([[a.count(i),i] for i in set(a)],key=lambda x: x[0],reverse=True)
try:
    print('?') if b[0][0]==b[1][0] else print(b[0][1])
except:
    print(b[0][1])