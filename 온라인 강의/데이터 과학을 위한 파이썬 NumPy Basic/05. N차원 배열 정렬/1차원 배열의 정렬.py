import numpy as np


# ### Section 4.N차원 배열 정렬
# ##### 4-1. 1차원 배열의 정렬


arr = np.random.randint(10,size=10)
print(arr)


print(np.sort(arr))#오름
print(np.sort(arr)[::-1]) #내림차순
print(arr)
arr = np.sort(arr) # 할당
print(arr) 
arr.sort() # 도 가능

