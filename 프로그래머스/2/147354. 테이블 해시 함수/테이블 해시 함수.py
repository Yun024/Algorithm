def solution(data, col, row_begin, row_end):
    
    sorted_data = sorted(data,key=lambda x: [x[col-1],-x[0]])
    mod_data = [sum([j%(i+1) for j in v]) for i,v in enumerate(sorted_data)]
    ans = 0
    for i in mod_data[row_begin-1:row_end]:
        ans ^= i
    
    return ans