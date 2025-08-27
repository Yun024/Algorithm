import sys,math
input = sys.stdin.readline

n = int(input().strip())
for i in range(1,n+1):
    s = input().strip()
    sex,mom,dad = s.split(' ')
    mom = list(map(int,mom.strip("\"").split("'")))
    dad = list(map(int,dad.strip("\"").split("'")))
    feet = (mom[0] + dad[0])*12
    inch = mom[1] + dad[1]
    if sex == 'B':
        ans = feet + inch + 5
    else:
        ans = feet + inch - 5
    ans /= 2
    ans1,ans2 = math.ceil(ans)-4,int(ans)+4
    print(f"Case #{i}: {ans1//12}'{ans1%12}\" to {ans2//12}'{ans2%12}\"")