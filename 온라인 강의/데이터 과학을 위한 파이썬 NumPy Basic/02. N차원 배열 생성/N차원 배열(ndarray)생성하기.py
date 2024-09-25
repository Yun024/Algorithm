import numpy as np


# ### Section 1.N차원 배열 생성
# ##### 1-1 N차원 배열(ndarray) 생성하기


# 1차원 배열
arr = np.array([1,2,3])
print(arr)

# 2차원 배열
arr = np.array([[1,2,3],
                [4,5,6]])
print(arr)


type([1,2,3])
type(arr)


tpl = (4,5,6)
arr = np.array(tpl)
print(arr)

lst = [1,2,3]
arr = np.array(lst)
print(arr)

lst2 = [[1,2,3],[4,5,6]]
arr2 = np.array(lst2)
print(arr2)


# shape 행열
arr1 = np.array([1,2,3])
arr2 = np.array([[1,2,3],[4,5,6]])

print(arr1.shape, arr2.shape)

# ndim 차원
print(arr1.ndim, arr2.ndim)

# size 원소의 개수
print(arr1.size, arr2.size)

