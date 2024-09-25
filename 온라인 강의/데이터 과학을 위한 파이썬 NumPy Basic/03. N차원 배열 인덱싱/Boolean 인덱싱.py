import numpy as np


# ### Section 2.N차원 배열의 인덱싱
# ##### 2-3. Boolean 인덱싱


arr = np.arange(1,5)
print(arr[[True,False,True,True]])


arr = np.array([[1,2,3,4],
               [5,6,7,8]])
print(arr[[True,False],True])


arr = np.array([[1,2,3,4],
               [5,6,7,8]])
print(arr[arr>3])
print(arr[arr<=2])

