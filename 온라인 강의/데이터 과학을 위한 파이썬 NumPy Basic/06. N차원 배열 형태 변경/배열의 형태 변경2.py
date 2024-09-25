import numpy as np


# ### Section 5.N차원 배열의 형태 변경
# ##### 5-2. 배열의 형태 변경2: resize(), ravel()


arr = np.arange(12)
print(arr)


arr.resize(3,4)
print(arr)


arr = arr.ravel() #1차원으로 변경
print(arr)


arr = np.arange(1,13)
print(arr)

arr = arr.reshape(3,-1) #-1을 넣으면 열이 자동으로 계산됨
print(arr)

arr = arr.reshape(3,2,-1)
print(arr)

# arr.reshape(3,-1,-1) # 두개의 -1은 계산할 수 없기 때문에 에러

