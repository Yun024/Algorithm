import numpy as np
import time


# ### Section 3.N차원 배열의 연산법
# ##### 3-6. 벡터 연산의 장점


arr = np.arange(99999999,dtype='int64')
# np.arange(99999999)으로 하면 정수형 int32데이터 타입에 의해 오버플로우가 발생해서 제대로 된 값이 나오지 않음


# for문 연산
sum = 0;
before = time.time()
for i in arr:
    sum +=i
after = time.time()
print(sum,after - before,"초")


# 벡터 연산
before = time.time()
sum = np.sum(arr)
after = time.time()
print(sum,after-before,'초')


arr1 = np.arange(99999999,dtype='int64')
arr2 = np.arange(99999999,dtype='int64')


# for문/ 2개의 배열의 dot product연산
sum = 0
before= time.time()
for j,i in zip(arr1,arr2):
    sum += i * j 
after = time.time()
print(sum, after- before, '초')


# 벡터 연산
before = time.time()
sum = np.dot(arr1,arr2)
after = time.time()
print(sum,after-before, '초')

