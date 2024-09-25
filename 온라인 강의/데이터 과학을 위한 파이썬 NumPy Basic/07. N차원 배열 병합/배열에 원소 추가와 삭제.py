import numpy as np


# ### Section 6.N차원 배열의 병합
# ##### 6-1. 배열에 원소 추가 및 삭제


# python list
arr = list(range(9))
arr.insert(2,50)
print(arr)


# 1차원 배열
arr = np.arange(1,9)
arr = np.insert(arr,2,50)
print(arr)


# 2차원 배열
arr = np.arange(1,13).reshape(3,4)
arr = np.insert(arr,2,50, axis = 1) 
## axis를 생략하면 1차원배열로 변형 후 insert실행
print(arr)


# delete()
arr = np.arange(1,13).reshape(3,4)
print(arr)

arr = np.delete(arr,2) 
# axis를 생략하면 1차원 배열로 변형 후 2번째 Index의 원소 삭제
print(arr)




