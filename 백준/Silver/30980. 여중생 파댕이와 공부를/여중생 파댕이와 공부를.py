import sys,re
input = sys.stdin.readline

n,m = map(int,input().split())
for idx in range(n*3):
    temp = input().strip()
    if idx%3 == 1:
        calcul = re.findall("[0-9]+",temp)
        ans = []
        for n in range(3):
            res = ""
            for i in range(0,len(calcul),3):
                a,b,c = calcul[i], calcul[i+1], calcul[i+2]
                if not n:
                    if int(a) + int(b) == int(c):
                        strings = "." + "*"*(len(a+b+c)+2)
                        res += strings.ljust(8,".")
                    else:
                        res += ".../...."
                elif n == 1:
                    if int(a) +  int(b) == int(c):
                        strings = "*" + a + "+" + b + "=" + c + "*"
                        res += strings.ljust(8,".")
                    else:
                        strings = "." + a + "/" + b + "=" + c
                        res += strings.ljust(8,".")
                else:
                    if int(a) + int(b) == int(c):
                        strings = "." + "*"*(len(a+b+c)+2)
                        res += strings.ljust(8,".")
                    else:
                        res += "./......"
            print(res)