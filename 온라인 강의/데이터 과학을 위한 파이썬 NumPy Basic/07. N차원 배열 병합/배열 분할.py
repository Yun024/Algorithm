import numpy as np


# ### Section 6.N차원 배열의 병합
# ##### 6-3. 배열의 분할


# 2차원 배열
arr = np.arange(1,13).reshape(3,4)
print(arr)

# vsplit() => axis=0
arr_vsplit = np.vsplit(arr,3) # 3행이므로 홀수
print(arr_vsplit)

# hsplit() => axis=1 
arr_hsplit = np.hsplit(arr,2) # 4열이므로 짝수 
print(arr_hsplit)


# 3차원 배열
arr = np.random.randint(0,10,[4,6,8])
print(arr)


arr_vsplit = np.vsplit(arr,2)
print(arr_vsplit)


arr_hsplit = np.hsplit(arr,2)
print(arr_hsplit)





