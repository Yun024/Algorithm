## URL: https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/

from collections import Counter
def solution(A):
    A.sort()
    if A[0] != 1 or Counter(A).most_common()[0][1] > 1:
        return 0
    for i in range(1,len(A)):
        if A[i] != A[i-1] +1:
            return 0
    return 1

print(solution([3,4,5]))


"""
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""
