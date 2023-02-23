def solution(s):
    ans = list(map(lambda x: int(x),s.split()))
    return str(min(ans)) +  " " +  str(max(ans))