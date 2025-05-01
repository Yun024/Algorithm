import sys

# 입력 받기
num_list = [int(line.strip()) for line in sys.stdin if line.strip()]

# 점수와 인덱스 묶기
ans = [[j+1, i] for j, i in enumerate(num_list)]

# 점수 기준으로 정렬하고 상위 5개 선택
ans = sorted(ans, key=lambda x: x[1], reverse=True)[:5]

# 점수 총합 및 인덱스 정렬
score = [i[1] for i in ans]
seq = [i[0] for i in ans]

print(sum(score))
print(*sorted(seq))
