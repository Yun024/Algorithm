import numpy as np


# ### Section 3.N차원 배열의 연산법
# ##### 3-1. 배열의 연산1: 사칙연산/제곱/제곱근/몫/나머지


arr1 = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
arr2 = np.full((3,3),2)


#덧셈
print(arr1+arr2)
print(np.add(arr1,arr2))


#뺄셈
print(arr1-arr2)
print(np.subtract(arr1,arr2))


#곱셈
print(arr1*arr2)
print(np.multiply(arr1,arr2))


#나눗셈
print(arr1/arr2)
print(np.divide(arr1,arr2))


#제곱연산
print(arr1 ** 5)
print(np.square(arr1))


#제곱근
print(np.sqrt(arr1))


#몫
print(arr1//2)

#나머지
print(arr1 %2)

