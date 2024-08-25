num, base = map(int, input().strip().split(' '))
print(int(str(num),base))

# int(str,몇진수) => 10진수로 변환
# print(sum(([int(i)*base**j for j,i in enumerate(str(num)[::-1])])))