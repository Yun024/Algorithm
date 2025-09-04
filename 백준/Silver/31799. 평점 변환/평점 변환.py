import sys

input = sys.stdin.readline
n = int(input().strip())
grades = input().strip()

def trans_grade(n):

    before = before_grade[n-1]
    now = before_grade[n]

    if now in ["C+","C0","C-"]:
        return "B"
    elif now in ["B0","B-"]:
        if not n or before in ["C+","C0","C-"]:
            return "D"
        else:
            return "B"
    elif now in ["A-","B+"]:
        if not n or before in ["B0","B-","C+","C0","C-"]:
            return "P"
        else:
            return "D"
    elif now == "A0":
        if not n or before in ["A-","B+","B0","B-","C+","C0","C-"]:
            return "E"
        else:
            return "P"
    return "E"
    
before_grade = []
temp = ""

for grade in grades:
    if grade.isalpha() and temp:
        if len(temp) == 1:
            temp += "0"
        before_grade.append(temp)
        temp = grade
    else:
        temp += grade

if len(temp) == 1:
    temp += "0"
before_grade.append(temp)

print(''.join([trans_grade(num) for num in range(n)]))
    


        