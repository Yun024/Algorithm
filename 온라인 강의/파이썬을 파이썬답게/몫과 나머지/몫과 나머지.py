a, b = map(int, input().strip().split(' '))
print(*divmod(a,b))

# *는 리스트를 괄호제거하고 각각의 문자를 공백으로 한칸 띄운 후 출력함
# divmod는 몫과 나머지를 계산하는 함수
# print(a//b, a%b)