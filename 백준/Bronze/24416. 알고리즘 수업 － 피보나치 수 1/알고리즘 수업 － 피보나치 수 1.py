def fib(n):
    if (n == 1 or n == 2):
        return 1
    else:
        return (fib(n-1) +  fib(n-2))

def fibo(n):
    f = [0] * (n+1)
    f[1] = f[2] = 1
    global cnt
    for i in range(3,n+1):
        cnt +=1
        f[i] = f[i-1] + f[i-2]
    return f[n]

num = int(input())
cnt = 0

print(fibo(num),cnt)