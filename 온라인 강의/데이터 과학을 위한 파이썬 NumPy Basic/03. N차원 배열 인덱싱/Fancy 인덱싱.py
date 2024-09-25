import numpy as np


# ### Section 2.N차원 배열의 인덱싱
# ##### 배열의 2-2. Fancy 인덱싱


# 1차원 배열
arr = np.arange(5,31,5)
print(arr[[0,2,4]])


# 2차원 배열
arr = np.array([[5,10,15,20],
                [25,30,35,40],
                [45,50,55,60]])
print(arr[[0,2],2:])
print(arr[1:,[2,3]])

