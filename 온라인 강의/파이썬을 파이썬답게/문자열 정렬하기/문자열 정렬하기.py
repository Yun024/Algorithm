s, n = input().strip().split(' ')
n = int(n)
# format을 이용한 정렬(print함수 여러 번 실행)
print(("{0:<"+str(n)+"}").format(s))
print(("{0:^"+str(n)+"}").format(s))
print(("{0:>"+str(n)+"}").format(s))

# print(s.ljust(n)+'\n'+s.center(n)+'\n'+s.rjust(n)) 
# 문자열 사이에 \n을 넣음으로 줄바꿔서 출력이 가능
