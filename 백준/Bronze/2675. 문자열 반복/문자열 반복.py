for i in range(int(input())):
    b,c = map(str,input().split())
    print(''.join([i*int(b) for i in c]))