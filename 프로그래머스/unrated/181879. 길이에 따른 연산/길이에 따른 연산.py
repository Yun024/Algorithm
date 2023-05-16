from functools import reduce
def solution(num_list):
        return   reduce(lambda x,y: x*y , num_list) if len(num_list) <= 10 else sum(num_list)
    
        
import math
def solution(num_list):
        return   math.prod(num_list) if len(num_list) <= 10 else sum(num_list)
    
