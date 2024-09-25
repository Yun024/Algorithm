import numpy as np


# ### Section 1.N차원 배열 생성
# ##### 1-4 특정 범위의 값을 가지는 N차원 배열 생성하기


lst = list(range(0,9,2))
print(lst)


arr = np.arange(9) # start, stop, step
print(arr)

arr = np.arange(3,12)
print(arr)

arr = np.arange(3,13,3)
print(arr)


# np.linsapce() num = 균등한 간격으로 배열 생성
# linspace의 stop값은 값 포함
arr = np.linspace(0,100,11) # start, stop, num
print(arr)

arr = np.linspace(0,100,250)
print(arr)


# np.logspace()
arr = np.linspace(1,10,10)
print(arr, end="\n\n")

arr = np.logspace(1,10,10, base =2 ) # base는 로그의 밑수
print(arr)

arr = np.logspace(1,10,10) # base를 생략하면 상용로그 밑수= 10
print(arr)




