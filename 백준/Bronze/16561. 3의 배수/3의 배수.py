n = int(input())

count = 0
for i in range(3, n, 3):
    for j in range(3, n - i, 3):
        k = n - i - j
        if k >= 3 and k % 3 == 0:
            count += 1

print(count)
