from collections import Counter

def solution(s1, s2):
    f = lambda s: [s[i:i+2].lower() for i in range(len(s)-1) if s[i:i+2].isalpha()]
    ca, cb = Counter(f(s1)), Counter(f(s2))
    inter = sum((ca & cb).values())
    union = sum((ca | cb).values())
    return int(inter / union * 65536) if union else 65536


# def solution(str1, str2):
#     from collections import Counter
#     a = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
#     b = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
#     ca, cb= Counter(a) , Counter(b)
#     up = list(set(a) & set(b)) 
#     down = list(set(a) | set(b))
#     return int(sum([min(ca[i],cb[i]) for i in up]) / sum([max(ca[i],cb[i]) for i in down]) * 65536) if up or down else 65536