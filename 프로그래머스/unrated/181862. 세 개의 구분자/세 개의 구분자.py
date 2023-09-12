def solution(myStr):
    word = ""
    answer = []
    key = ["a","b","c"]
    for i in myStr:
        if i not in key:
            word += i
        else:
            if len(word) !=0 :  answer.append(word)
            word = ""
    answer.append(word)
    return answer if answer != [""] else ["EMPTY"]
    