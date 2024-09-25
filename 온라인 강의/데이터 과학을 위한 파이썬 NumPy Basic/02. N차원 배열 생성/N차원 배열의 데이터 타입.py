import numpy as np


# ### Section 1.N차원 배열 생성
# ##### 1-2 N차원 배열의 데이터 타입


arr = np.array([1,2,3], dtype = np.float)
print(arr, arr.dtype) 

arr = np.array([1.1,2.2,3.3], dtype = np.int)
print(arr, arr.dtype) 


arr = np.array([0,1,1], dtype = np.bool)
print(arr, arr.dtype) 
# float64에서 64는 해당 어레이의 강 성분을 표현 할때 메모리상에서 몇비트를 사용할 것인지
# 숫자가 크면 클수록 해당 어레이의 길이가 긴 정수 혹은 실수를 사용할 수 있음


# 기존의 데이터 타입을 변경할 때는 astype
arr = np.array([0,1,2,3])
print(arr, arr.dtype)

arr = arr.astype(np.float32)
print(arr,arr.dtype)


# 데이터 타입이 혼재하는 경우
# numpy는 한 가지 데이터 타입만 가질 수 있음
arr = np.array([1,2,3.4])
print(arr, arr.dtype)

arr1 = np.array([1,2,3.4,'64']) #문자열에 맞춰 변경
print(arr1,arr1.dtype) # 유니코드 형식으로 변경

arr2 = np.array([1,2,3.4,'64. 문자열']) # dtype= int넣으면 에러 발생
print(arr2, arr2.dtype)



