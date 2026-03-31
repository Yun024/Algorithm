from __future__ import annotations

def normalize_ws(s: str) -> tuple[str, int]:
    
    """
    1) 공백 정규화 + 단어 수 계산
    s="  a\t b   c  " → ("a b c", 3)
    s="\n\t " → ("", 0)
    """
    res = s.split()
    cnt = len(res)
    ans = ' '.join(res)
    return ans,cnt

def unique_keep_order(arr: list[int]) -> list[int]:
    
    """
    2) 중복 제거(첫 등장 순서 유지)
    [3, 1, 3, 2, 1] → [3, 1, 2]
    [] → []
    """
    dic = {}
    res = []
    for a in arr:
        if not dic.get(a):
            res.append(a)
            dic[a] = 1
    return res

def is_valid_brackets(s: str) -> bool:
    """
    3) 괄호 문자열 유효성 검사
    "([]){}" → True
    "(]" → False
    "(((" → False
    "" → True
    """
    ans = []
    dic = {")":"(", "]":"[", "}":"{"}

    for i in s:
        if i not in dic:
            ans.append(i)
        else:
            if not ans or ans[-1] != dic[i]:                
                return False
            else:
                ans.pop()
        
    return True if not ans else False

def parse_query(qs: str) -> dict[str, list[str]]:
    """
    4) 쿼리 스트링 파싱
    a=1&b=2&b=3" -> {"a":["1"], "b":["2","3"]}
    """
    ans = {}
    if not qs:
        return ans

    for s in qs.split("&"):
        res = s.split("=")
        if ans.get(res[0]):
            ans[res[0]].append(res[1])
        else:
            ans[res[0]] = [res[1]]
    return ans

def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    """
    5) 정렬된 두 리스트 병합(sort, sorted 금지)
    [1,3], [2,4] → [1,2,3,4]
    """
    now_a, now_b = 0,0
    length_a, length_b = len(a), len(b)
    ans = []

    while now_a < length_a and now_b < length_b: 
        if a[now_a] > b[now_b]:
            ans.append(b[now_b])
            now_b += 1
        else:
            ans.append(a[now_a])
            now_a += 1
    
    ans += a[now_a:]
    ans += b[now_b:]

    return ans
