import numpy as np


### Section 7.NumPy 실습 예제
##### 7-3. 실습 예제7~10


# 실습 예제7
'''
다음 두 행렬에 대하여 내적 연산을 수행한 결과값을 출력하시오
(단, 결과의 소수점 아래는 제거한다)
'''
arr1 = np.array([2.1, 3.5, 4.2, 2.7, 2.3, 1.9]).reshape(3,2)
arr2 = np.array([5,2,3,1,3,5]).reshape(2,3)
print(arr1,'\n\n',arr2)


print(np.dot(arr1,arr2).astype(int))
np.trunc(np.dot(arr1,arr2)) #버림은 trunc, 내림은 floor -일때 수치바뀜


# 실습 예제8
'''
조건 연산자를 활용한 Boolean 인덱싱을 이용하여 다음 배열의 원소들 중
2와 5의 배수만 추출한 결과를 오름차순 정렬하여(2,4)행렬로 출력하시오
'''
arr = np.arange(1,13).reshape(3,4)
arr


np.sort(np.append(arr[arr%2==0],arr[arr%5==0])).reshape(2,4)


# 실습 예제9
'''
10진수 100이상 150미만 사이에 존재하는 정수를 무작위로 추출하여 (3,10)
형태의 행렬로 만들고 행과 열을 전치한 결과를 출력하시오
'''
result = np.random.randint(100,150,(3,10))
result.T
np.transpose(result)


# 실습 예제10
'''
10진수 10~20 사이에 존재하는 실수형의 수를 무작위로 10000개 추출하여
100개의 구간에 그래프로 시각화하시오. (단, 무작위 실수 값은 균등한
비율로 추출해야 하며 그래프 시각화 도구는 pyplot모듈을 사용할 것)
'''


import matplotlib.pyplot as plt
# 10~20 사이의 실수를 가지는 난수 생성
np.random.rand(10000)  # 0~1의 난수 10000개
arr= 10 + np.random.rand(10000)*10 # 10에서 20사이 난수


plt.hist(arr,bins=100)
plt.show()





