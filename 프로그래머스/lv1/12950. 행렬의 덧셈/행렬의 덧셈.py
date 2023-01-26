
def solution(arr1, arr2):
    final =[] 
    answer = [i+j for i,j in zip(sum(arr1,[]),sum(arr2,[]))]
    key = len(answer)/len(arr1)
    for i in range(len(arr1)):
        final.append(answer[:int(key)])
        answer = answer[int(key):]
    return final