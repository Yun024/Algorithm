def solution(numbers):
    string = ["zero","one" ,"two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    dic = {}
    for i in range(len(string)):
        dic.update({string[i]:str(i)})
    
    answer = []
    while len(numbers) != 0:
        for i in range(3,6):
            if numbers[:i] in dic:
                answer.append(numbers[:i])
                numbers = numbers[i:]
    return int(''.join([dic[i] for i in answer]))