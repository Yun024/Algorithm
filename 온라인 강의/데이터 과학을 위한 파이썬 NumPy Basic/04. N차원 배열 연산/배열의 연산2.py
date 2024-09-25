import numpy as np


# ### Section 3.N차원 배열의 연산법
# ##### 3-2. 배열의 연산2: 내적(dot product)/절댓값/올림/내림/반올림/버림


# 1차원 행렬
arr1 = np.arange(2,5)
arr2 = np.arange(1,4)
##(1*2) + (3*2) + (4*3)
print(np.dot(arr1,arr2)) 

# 2차원 행렬
arr1 = np.array([[1,2],
                [4,5]])
arr2 = np.array([[1,2],
                [0,3]])
'''
[[a,b] [e,f]     [[ae + bg, af + bh]
 [c,d] [g,h]] =>  [ce + dg, cf + dh]]

'''
print(np.dot(arr1,arr2))


# 절댓값
arr1 = np.array([[1,-2],
                [-4,5]])
print(np.abs(arr1))


# 올림
arr1 = np.array([[1.932, -2.339],
                [-4.145, 5.206]])
print(np.ceil(arr1))

# 내림
print(np.floor(arr1))

# 반올림 
print(np.round(arr1))

# 버림
print(np.trunc(arr1))

