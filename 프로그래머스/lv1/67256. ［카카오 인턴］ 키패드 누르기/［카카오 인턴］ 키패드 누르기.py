keypad = [1,2,3,4,5,6,7,8,9,"*",0,"#"]
def key_diff(a,b):
    answer = abs(keypad.index(a) - keypad.index(b))// 3 +\
    abs(keypad.index(a) - keypad.index(b))% 3 
    return answer

def solution(numbers, hand):
    answer =""
    l,r = "*", "#"
    left = [1,4,7]
    right = [3,6,9]
    for i in numbers:
        if i in left:
            answer += "L"
            l = i
        elif i in right:
            answer += "R"
            r = i
        else:
            if key_diff(i,l) == key_diff(i,r):
                answer += hand[0].upper()
                if hand[0].upper() == "R":
                    r = i
                else:
                    l = i
            elif min(key_diff(i,l),key_diff(i,r))== key_diff(i,l):
                answer += "L"
                l = i
            else:
                answer += "R"
                r = i
    return answer
                
                