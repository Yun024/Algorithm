import numpy as np


# ### Section 5.N차원 배열의 형태 변경
# ##### 5-1. 배열의 형태 변경1: reshape()


arr = np.arange(12)
print(arr,arr.ndim)


#size가 맞지 않을 경우 에러 발생
## arr.reshape(2,3)
arr = arr.reshape((3,4))
print(arr, arr.ndim)


arr = arr.reshape((2,3,2))
print(arr,arr.ndim)


arr = arr.reshape((2,2,1,3))
print(arr, arr.ndim)


# curse of dimensionality 
# 차원의 저주
## 데이터들 사이의 거리가 커지는 현상

