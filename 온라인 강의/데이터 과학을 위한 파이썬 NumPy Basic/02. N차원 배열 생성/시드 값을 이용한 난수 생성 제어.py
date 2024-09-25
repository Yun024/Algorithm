import numpy as np


# ### Section 1.N차원 배열 생성
# ##### 1-6 시드 값을 이용한 난수 생성 제어


arr = np.random.rand(10)
print('난수 발생1 \n', arr)


arr = np.random.rand(10)
print('난수 발생2 \n', arr)


# 시드를 통해 동일한 난수가 나올 수 있도록 지정가능
np.random.seed(1)
arr = np.random.rand(10)
print("난수 발생1 \n", arr)


np.random.seed(10)
arr = np.random.rand(10)
print("난수 발생2 \n", arr)

