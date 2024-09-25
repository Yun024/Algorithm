
import numpy as np
# 난수를 시각화해서 보기위한 라이브러리
import matplotlib.pyplot as plt


# ### Section 1.N차원 배열 생성
# ##### 1-5 난수로 이루어진 N차원 배열


# np.random.normal()
# loc, scale, size 정규분포의 평균, 표준편차, 추출할 표본의 개수
# size부분을 shape으로 지정하면 행열로 이루어진 난수 생성
arr= np.random.normal(0,1,10)
print(arr)

arr = np.random.normal(0,1,(2,3))
print(arr)


arr = np.random.normal(0,1,1000000)
plt.hist(arr,bins=100) # bins 난수를 몇개의 구간으로 구분해서 보여줄지
plt.show()


# np.random.rand() : 0부터 1 균등분포
arr = np.random.rand(1000)
plt.hist(arr,bins=100)
plt.show()


# np.random.randn() #가우시안 분포, -1부터 1 사이의 값을 정규분포
arr = np.random.randn(100000)
plt.hist(arr,bins=100)
plt.show()


# np.random.randint() 랜덤한 정수 출력
# size에 shape도 가능
arr = np.random.randint(low=1, high=5, size=10) 
print(arr)

np.random.randint(5) # 0부터 5사이의 1개의 값 출력 low와 size는 default


arr = np.random.randint(100,200,1000)
plt.hist(arr,bins=100)
plt.show()

