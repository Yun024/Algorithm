import numpy as np


# ### Section 5.N차원 배열의 형태 변경
# ##### 5-3. 배열의 형태 변경3: expand_dims(), squeeze()


# expand_dims()
arr = np.array((1,2))
print(arr, arr.shape)

arr = np.expand_dims(arr,axis=0) # axis=1
print(arr,arr.shape)


# squeeze()
arr = np.array([[1,2]])
print(arr, arr.shape, arr.ndim)

arr = np.squeeze(arr, axis=0)
print(arr, arr.shape, arr.ndim)


arr = np.array([[[1],
                 [2],
                 [3]]])
print(arr, arr.shape, arr.ndim)

arr = np.squeeze(arr, axis=0)
print(arr, arr.shape, arr.ndim)


arr = np.array([[[1,2,3]]])
print(arr, arr.shape, arr.ndim)

arr = np.squeeze(arr, axis=1) # 0,1 둘 중 무엇을 입력해도 똑같은 결과
## X축과 Y축 모두 1,1이기 때문에 
print(arr, arr.shape, arr.ndim)

arr = np.squeeze(arr)
print(arr,arr.shape, arr.ndim)
# axis를 입력하지 않으면 1차원 배열로 축소

