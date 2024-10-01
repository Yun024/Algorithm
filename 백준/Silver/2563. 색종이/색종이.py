answer = [100*[0] for i in range(100)]
a = int(input())
for i in range(a):
    b,c = map(int,input().split())
    for row in range(b,b+10):
        for col in range(c,c+10):
            answer[row][col] = 1
print(sum([len([j for j in i if j==1]) for i in answer]))