def solution(number, limit, power):
    answer = [1]
    for i in range(2,number+1):
        ans = 2
        for j in range(2,int(i**0.5)+1):
            if i%j ==0:
                ans +=1
                if (j**2) != i :
                    ans +=1
        answer.append(ans)
    return sum([power if i>limit else i for i in answer])