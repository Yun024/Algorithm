import numpy as np


# ### Section 4.N차원 배열 정렬
# ##### 4-2. 2차원 배열의 정렬


arr = np.random.randint(15,size=(3,4))
print(arr)


print(np.sort(arr,axis=0))
print(np.sort(arr))
print(np.sort(arr,axis=None)) # 1차원 배열로 변경 후 오름차순


# argosrt()
## 정렬 전 인덱스위치를 출력해줌 
print(np.sort(arr,axis=1))
print(np.argsort(arr,axis=1))
print(np.sort(arr,axis=0))
print(np.argsort(arr,axis=0))


