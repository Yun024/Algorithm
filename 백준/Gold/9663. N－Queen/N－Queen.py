def backtrack(n, start, col, diag1, diag2):
    if start == n:
        global ans
        ans += 1
        return 
    
    for i in range(n):
        if not col[i] and not diag1[start + i] and not diag2[start - i + n - 1]:
            col[i] = True
            diag1[start + i] = True
            diag2[start - i + n - 1] = True

            backtrack(n, start + 1, col, diag1, diag2)

            col[i] = False
            diag1[start + i] = False
            diag2[start - i + n - 1] = False

n = int(input())
ans = 0
col = [False] * n
diag1 = [False] * (2 * n - 1)  # row + col (↘ 대각선)
diag2 = [False] * (2 * n - 1)  # row - col + (n-1) (↙ 대각선)

backtrack(n, 0, col, diag1, diag2)
print(ans)
