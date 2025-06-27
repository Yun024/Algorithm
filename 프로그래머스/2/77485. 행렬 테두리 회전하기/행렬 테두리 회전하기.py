def solution(rows, columns, queries):
    
    def outline(query):
        sx,sy,ex,ey = map(lambda x: x-1,query)
        dx = ex - sx
        dy = ey - sy
        nums = []
        for _ in range(dx):
            sx += 1
            nums.append(matrix[sx][sy])
        for _ in range(dy):
            sy += 1
            nums.append(matrix[sx][sy])
        for _ in range(dx):
            sx -= 1
            nums.append(matrix[sx][sy])
        for _ in range(dy):
            sy -= 1
            nums.append(matrix[sx][sy])
        result = min(nums)
        for _ in range(dy):
            sy += 1
            matrix[sx][sy] = nums.pop()
        for _ in range(dx):
            sx += 1
            matrix[sx][sy] = nums.pop()
        for _ in range(dy):
            sy -= 1
            matrix[sx][sy] = nums.pop()
        for _ in range(dx):
            sx -= 1
            matrix[sx][sy] = nums.pop()
        return result

    matrix = [[columns * r + c + 1 for c in range(columns)] for r in range(rows)]
    ans = []
    for query in queries:
        ans.append(outline(query))
    return ans
    
        