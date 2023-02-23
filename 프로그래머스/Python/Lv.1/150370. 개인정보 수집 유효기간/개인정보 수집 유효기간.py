def dt_spl(x):
    year,month,day = map(int,x.split("."))
    return year*12*28 + month * 28 + day 
    
def solution(today, terms, privacies):
    #최종풀이: 모든 달이 28일로 가정하기 때문에 숫자로 변환 후 문제해결
    today = dt_spl(today)
    term = dict([i.split() for i in terms])
    answer = []
    for i in privacies:
        x = i.split()
        answer.append(dt_spl(x[0]) + int(term[x[1]])*28 - 1)
    return [j+1 for j,i in enumerate(answer) if i<today]
    
#     최초풀이: 년,월,일 나누어 문자열 베이스로 문제해결
#     term = dict(i.split() for i in terms)
#     answer = []
#     for i in privacies:
#         z = i.split()
#         key = int(z[0][5:7]) + int(term[z[1]])
#         day = int(z[0][8:]) -1 
#         day = "28" if day == 0 else str(day).rjust(2,"0")
#         month = (key-1)%12 if day == "28" else key%12
#         month = "12" if month == 0 else str(month).rjust(2,"0")
#         if key < 13 :
#             year = str(int(z[0][:4]))
#         else:
#             year= str(int(z[0][:4]) + key//12 - 1) if month=="12" else str(int(z[0][:4]) + key//12)
#         answer.append(year+month+day)
        
#     return [j+1 for j,i in enumerate(answer) if int(i)< int(today.replace(".",""))]