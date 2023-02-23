from collections import Counter
def solution(id_list, report, k):
    report = list(set(report))
    answer = Counter(list(map(lambda x: x.split()[1],report))) 
    ans = [j for j,i in answer.items() if i>=k]
    final = [i.split()[0] for i in report if i.split()[1] in ans]
    return [final.count(i) for i in id_list]
    
    
    
    