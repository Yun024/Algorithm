from collections import Counter
def solution(participant, completion):
    # 모듈 사용 후 풀이
    return list((Counter(participant) - Counter(completion)).keys())[0]
        
    # 모듈 사용 전 풀이/ dict사용
    # _participant = dict(zip(range(len(participant)),sorted(participant)))
    # _completion = dict(zip(range(len(completion)),sorted(completion)))
    # if len(_completion)==0:
    #     return _participant[0]
    # else:
    #     for i in range(len(_completion)):
    #         if _participant[i] != _completion[i]:
    #             return _participant[i]
    # return _participant[i+1]
    
            
    