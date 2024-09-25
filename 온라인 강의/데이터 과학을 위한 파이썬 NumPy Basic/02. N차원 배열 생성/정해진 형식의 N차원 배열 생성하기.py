import numpy as np


# ### Section 1.N차원 배열 생성
# ##### 1-3 정해진 형식의 N차원 배열 생성하기


# np.zeros() : 모든 원소들이 0으로 되어 있는 배열 생성
arr = np.zeros([2,2]) # 행열 입력
print(arr)


# np.ones() : 모든 원소들이 1로 되어 있는 배열 생성
arr = np.ones([3,5])
print(arr)


# np.full() : 모든 원소들이 지정된 fill value로 채워짐
arr = np.full([2,3],5)
print(arr)


# np.eye() : 행을 n, 열 m일때 대각원소가 1인 배열 생성
# k에 -1도 가능 
# N값만 넣으면 정방행렬 나옴
arr = np.eye(3,4,k = 0)
print(arr)


# 지정된 배열과 동일한 행열을 갖도록 만드는 함수
arr = np.array([[1,2,3],[4,5,6]])


# np.zeros_like() 원소 0
arr_z = np.zeros_like(arr)
print(arr_z)


# np.ones_like()
arr_o = np.ones_like(arr)
print(arr_o)


# np.full_like()
arr_f = np.full_like(arr,9)
print(arr_f)






