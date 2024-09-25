import numpy as np


# ### Section 3.N차원 배열의 연산법
# ##### 3-3. 배열의 연산3: min/max/sum/mean/std/cumsum/median


arr = np.array([[1,2,3],
              [0,1,4]])


# min()
print(np.min(arr))
print(arr.min())
print(arr.min(axis=0)) # axis= 0은 열계산 , axis=1 은 행 계산


# max()
print(np.max(arr))
print(arr.max())
print(arr.max(axis=0))


# sum()
print(np.sum(arr))
print(arr.sum())
print(arr.sum(axis=0))


# mean()
print(np.mean(arr))
print(arr.mean())
print(arr.mean(axis=1))


# std()
print(np.std(arr))
print(arr.std())
print(arr.std(axis=0))


# cumsum() 누적합계산
print(np.cumsum(arr))
print(arr.cumsum())
print(arr.cumsum(axis=0))
print(arr.cumsum(axis=1))


# median()
arr = np.array([[1,2,3],
               [0,1,4],
               [1,5,2]])
print(np.median(arr))
print(np.median(arr,axis=0))
print(np.median(arr,axis=1))

