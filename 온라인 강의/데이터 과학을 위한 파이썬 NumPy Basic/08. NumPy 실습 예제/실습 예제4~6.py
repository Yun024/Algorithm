import numpy as np


### Section 7.NumPy 실습 예제
##### 7-2. 실습 예제4~6


#실습 예제4
'''
다음과 같은 numpy.array가 존재한다. 이 배열을 행을 기준으로 3개의 배열로
분할하여 분할된 각 배열의 원소들을 제곱한 결과를 다시 원본 배열에 행을 
기준으로 병합하시오.(단, 마지막 출력 결과는 원본 배열과 같아야 한다)
'''
arr = np.arange(2,20,2).reshape((3,3))
arr


arr_vsplit = np.vsplit(arr,3)
print(arr_vsplit)
arr1 = np.square(arr_vsplit)
print(arr1)

#차원축소
result = np.squeeze(arr1,axis=1)
print(result)
print(arr1.reshape(3,3))

#행을 기준으로 병합 
np.append(arr,result,axis=0)
np.vstack((arr,result))
np.concatenate((arr,result))


# 실습 예제5
'''
삼각함수의 특수각(0,30,60,90)을 numpy,array로 생성한 후 특수각에 
해당하는 sin,cos,tan 값을 각각 구하여 파이썬 List에 담은 다음 해당
list에 들어있는 값들을 출력하시오(단, 값이 무한대라면 'INF' 문자열 출력)
'''
arr = np.arange(0,91,30)
arr


lst = []
lst.append(np.sin(arr * np.pi / 180))
lst.append(np.cos(arr * np.pi / 180))
lst.append(np.tan(arr * np.pi / 180))


for i in lst:
    for j in i:
        if j > 99999999:
            print('INF')
        else:
            print(j)


# 실습 예제6
'''
numpy.array를 이용하여 다음과 같은 패턴을 출력하시오
(단, 출력 시 반복문을 사용하여 출력한다)
'''
arr1 = np.zeros((7,7),dtype=int)


arr1[::2,1::2] =1
arr1[1::2,::2]=1


for i in range(7):
    for j in range(7):
        print(arr1[i,j],end=" ")
    print()


for i in arr1:
    print(*i)





