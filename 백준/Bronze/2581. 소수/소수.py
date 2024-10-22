a,b = int(input()),int(input())
answer = []
for i in range(max(2,a),b+1):
    answer.append(i)
    for j in range(2,i//2+1):
        if i%j == 0:
            answer.pop()
            break
print(sum(answer),answer[0]) if answer else print(-1)