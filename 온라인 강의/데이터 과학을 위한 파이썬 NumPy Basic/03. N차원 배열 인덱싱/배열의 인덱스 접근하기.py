import numpy as np


# ### Section 2.N차원 배열의 인덱싱
# ##### 2-1. 배열의 index 접근하기


# 1차원 배열
arr = np.arange(0,10)
print(arr)


print(arr[3])
print(arr[1])
#print(arr[10]) # 10번째 Index없음 0~9존재
print(arr[-1]) 
print(arr[-3])
print(arr[-10]) # -는 -1부터시작해서 -10가능


# 2차원 배열
arr = np.array([[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12]])
print(arr,arr.shape,arr.ndim)
print(arr[0][3]) # 4에 접근하려면 [0,3]가능


arr = np.arange(0,10)
print(arr[3:8]) #3이상 8미만
print(arr[3:])
print(arr[:7]) #7미만
print(arr[:-1]) #-1미만


arr = np.array([[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12]])
print(arr[0,:]) # 0번째 행 모든 원소 출력
print(arr[:,1]) # 1번째 열 모든 원소 출력


print(arr[:3,:]) #3미만 모든 행의 원소 출력
print(arr[:2,2:]) #2미만 모든 행의 2이상 열의 원소 출력

