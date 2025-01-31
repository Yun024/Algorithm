def solution(numbers, target):
    def dfs(index,cnt):
        if index >= len(numbers):
            return 1 if cnt ==target else 0
        return dfs(index+1, cnt+numbers[index]) + dfs(index+1, cnt - numbers[index])
    return dfs(0,0)
            