
def solution(arr1, arr2):
    ans = []
    for i in arr1:
        middle = []
        for c in range(len(arr2[0])):
            sums = 0
            for n in range(len(arr1[0])):
                sums += i[n] * arr2[n][c]
            middle.append(sums)
        ans.append(middle)
    return ans
            
            
            
        
    
    
    return arr2[0]
            
                
            
    
            
                
    
        