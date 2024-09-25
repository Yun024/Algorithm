import numpy as np


# ### Section 7.NumPy 실습 예제
# ##### 7-1. 실습 예제1~3


# 실습 예제1
## 원소가 모두 3인 (3,4,5) 형태의 numpy,array를 출력하세요
arr = np.full((3,4,5),3)
print(arr)


# 실습 예제2
'''
정수 -50 ~ 50의 범위 안의 난수로 이루어진(4,5)형태의 Numpy.array를 
출력하고 행을 기준으로 오름차순 정렬한 결과와 전체 배열을 1차원
배열로 변경하여 오름차순 정렬한 결과를 출력하시오.
'''
arr = np.random.randint(-50,50,(4,5))
print(arr)
print(np.sort(arr,axis=0))

# 1차원으로 배열 변경 이후 오름차순 정렬
print(np.sort(arr.reshape(-1)))
print(np.sort(arr,axis=None))
print(np.sort(np.ravel(arr)))


# 실습 예제3
'''
다음과 같은 파이썬 list가 존재한다. list 안에 있는 각 Numpy.array의 
원소들의 평균값과 표준편차, 중앙값을 순서대로 구하여 구한 순서대로 
원소가 이루어진 새로운 List를 구성하고 출력하시오
'''
py_list = [np.full(3,8),
          np.array([33,-15,26]),
          np.linspace(17,26,3)]


arr = []
for i in py_list:
    arr.append(np.mean(i))
    arr.append(np.std(i))
    arr.append(np.median(i))
arr




