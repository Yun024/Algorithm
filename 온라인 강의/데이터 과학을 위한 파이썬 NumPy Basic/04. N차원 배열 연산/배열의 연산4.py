import numpy as np


### Section 3.N차원 배열의 연산법
##### 3-4. 배열의 연산4: 비교 연산/ 삼각 함수


# 비교 연산
arr1 = np.array([[1,2,3],
                [4,5,6]])
arr2 = np.array([[1,0,3],
                 [4,-2,9]])
print(arr1== arr2)
print(arr1>arr2)
print(np.array_equal(arr1,arr2)) #전체 배열이 같은지 비교 


# 삼각함수
arr = np.array([[1,2,3],
               [4,5,6]])
# sin()
print(np.sin(arr))
# cos()
print(np.cos(arr))
# tan()
print(np.tan(arr))
# pi
print(np.pi)

