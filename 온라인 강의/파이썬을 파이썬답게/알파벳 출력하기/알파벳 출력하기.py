num = int(input().strip())

# 모듈사용
# import string  
# lower = string.ascii_lowercase
# upper = string.ascii_uppercase

# print(lower if num==0 else upper)

# chr사용 A= 65, a = 97, 총 알파벳 개수 25
A,a = 65,97
if num == 0 :
    print(''.join([chr(i) for i in range(a,a+26)]))
else :
    print(''.join([chr(i) for i in range(A,A+26)]))

# 노가다
# print('abcdefghijklmnopqrstuvwxyz' if num==0 else 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')