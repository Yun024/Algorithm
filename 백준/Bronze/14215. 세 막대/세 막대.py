a,b,c = sorted(map(int,input().split()))    
print(a+b+a+b-1 if a+b <= c else a+b+c)