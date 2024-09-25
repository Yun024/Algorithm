import numpy as np


# ### Section 5.N차원 배열의 형태 변경
# ##### 5-4. 전치행렬(Transpose Matrix)


# 대각선을 기준으로 위치를 변경 (반 접는다생각)
## a12 => a21, a32=> a23


arr = np.array([[1,2],
               [3,4]])
print(arr.T)
print(np.transpose(arr))


arr = np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
print(arr.T)


# 정방행렬: 정사각형, 
arr = np.array([[1,2],
               [3,4],
               [5,6]])
print(arr.T) # 행렬전환


arr2 = np.full([3,2],2)
# print(arr.dot(arr2)) 행과 열의 갯수가 동일해야 연산됨, 에러발생


print((arr.T).dot(arr2)) # 행렬을 전환하여 연산하면 연산 가능 

