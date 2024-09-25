import numpy as np


# ### Section 3.N차원 배열의 연산법
# ##### 3-5. 브로드캐스팅(Broadcasting)


# 행,열이 같지 않을때 자동으로 행열을 확장하여 배열 연산 실행


arr1 = np.array([[0,0,0],
                [1,1,1],
                [2,2,2]])
arr2 = np.arange(5,8)
print(arr1+arr2)


arr1 = np.ones(3)
arr2 = np.array([[0],[1],[2]])
arr3 = np.array([1])
print(arr1+arr2)
print(arr1+arr3)

