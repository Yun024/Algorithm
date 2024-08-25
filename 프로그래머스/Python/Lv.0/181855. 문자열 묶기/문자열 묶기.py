from collections import Counter
def solution(strArr):    
    answer = [len(i) for i in strArr]
    
    return Counter(answer).most_common()[0][1]