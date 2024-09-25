import numpy as np


# ### Section 6.N차원 배열의 병합
# ##### 6-2. 배열 간의 병합


# append()
arr1 = np.arange(1,13).reshape(3,4)
arr2 = np.arange(13,25).reshape(3,4)

print(arr1)
print(arr2, end="\n\n")

# axis = 0
arr3 = np.append(arr1,arr2,axis=1)
## axis를 생략하면 1차원 배열로 변형 후 병합 실행
print(arr3,end="\n\n")


# vstack(). hstack()
arr1 = np.arange(1,7).reshape(2,3)
arr2 = np.arange(7,13).reshape(2,3)

arr3 = np.vstack([arr1,arr2])
print(arr3)

arr3 = np.hstack([arr1,arr2])
print(arr3)


# concatenate()
arr1 = np.arange(1,7).reshape(2,3)
arr2 = np.arange(7,13).reshape(2,3)

arr3 = np.concatenate([arr1,arr2],axis=0)
print(arr3)





