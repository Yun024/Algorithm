import sys
input = sys.stdin.readline

dic = {1:"Yakk",2:"Doh",3:"Seh",4:"Ghar",5:"Bang",6:"Sheesh"}
dic_equal = {1:"Habb Yakk",2:"Dobara",3:"Dousa",4:"Dorgy",5:"Dabash",6:"Dosh"}

t = int(input().strip())
for idx in range(t):
    a,b = map(int,input().split())
    if a == b:
        temp = dic_equal[a]
    else:
        if a in [5,6] and b in [5,6]:
            temp = "Sheesh Beesh"
        else:
            temp = dic[max(a,b)] + " " + dic[min(a,b)]
    print(f"Case {idx+1}: {temp}")