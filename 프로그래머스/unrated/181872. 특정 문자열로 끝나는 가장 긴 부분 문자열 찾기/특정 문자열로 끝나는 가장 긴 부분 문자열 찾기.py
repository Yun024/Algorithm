def solution(myString, pat):
    answer = myString[::-1].index(pat[::-1])
    return myString[:len(myString)-answer]