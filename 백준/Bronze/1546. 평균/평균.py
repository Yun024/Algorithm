input()
b = list(map(int,input().split()))

print(sum([i/max(b)*100 for i in b])/len(b))