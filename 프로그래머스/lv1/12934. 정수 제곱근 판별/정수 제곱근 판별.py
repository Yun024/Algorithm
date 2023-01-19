import numpy as np
def solution(n):
    answer = np.sqrt(n)
    return (answer+1)**2 if answer== int(answer) else -1