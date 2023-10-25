def solution(num_list):
    return max(sum([i for j,i in enumerate(num_list) if j%2==0]),sum([i for j,i in enumerate(num_list) if j%2!=0]))