a = int(input())
b = [2*i -1 for i in range(1,a+1)] 
c = [2*i -1 for i in range(1,a+1)][-2::-1]
d = b+c 
[print(((max(d)-i)//2)*' ' + '*'*i) for i in d]



