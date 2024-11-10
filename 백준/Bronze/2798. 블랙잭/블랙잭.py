a = int(input().split()[1])
b = list(map(int,input().split()))
answer= []
for i in range(len(b)):
    for j in range(i+1,len(b)):
        for u in range(j+1,len(b)):
            if sum([b[i],b[j],b[u]]) <= a:
                answer.append(sum([b[i],b[j],b[u]]))
print(max(answer))