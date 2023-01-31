
def solution(n, arr1, arr2):
    arr1 = [bin(i).replace("b","")[-n:] for i in arr1]
    arr2 = [bin(i).replace("b","")[-n:] for i in arr2]
    
    arr1 = ''.join([i if len(i)==n else "0"*(n-len(i))+i for i in arr1])
    arr2 = ''.join([i if len(i)==n else "0"*(n-len(i))+i for i in arr2])
    
    answer = ''.join(["0" if j=="0"and i=="0" else "1" for j,i in zip(arr1,arr2)]).replace("1","#").replace("0"," ")
    
    
    return [answer[i:i+n] for i in range(0,len(answer),n)]