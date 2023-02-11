# 첫번째 풀이
def solution(n, arr1, arr2):
    arr1 = ''.join([bin(i).replace("b","")[-n:].zfill(n) for i in arr1])
    arr2 = ''.join([bin(i).replace("b","")[-n:].zfill(n) for i in arr2])
    
    ### zfill로 대체 가능
    # arr1 = ''.join([i if len(i)==n else "0"*(n-len(i))+i for i in arr1])
    # arr2 = ''.join([i if len(i)==n else "0"*(n-len(i))+i for i in arr2])
    
    answer = ''.join(["0" if j=="0"and i=="0" else "1" for j,i in zip(arr1,arr2)]).replace("1","#").replace("0"," ")
    
    return [answer[i:i+n] for i in range(0,len(answer),n)]

# 두번째 풀이
def solution(n,arr1,arr2):
    answer =[]
    for j,i in zip(arr1,arr2):
        answer.append(bin(j|i)[2:].zfill(n).replace("1","#").replace("0"," "))
    return answer

# 세번째 풀이        
def solution(n, arr1,arr2):
    return [bin(j|i)[2:].zfill(n).replace("1","#").replace("0"," ") for j,i in zip(arr1,arr2)]
