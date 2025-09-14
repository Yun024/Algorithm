import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    sound, not_fox = [],[]
    while 1:
        temp = input().strip()
        if "goes" in temp:
            not_fox.append(temp.split("goes")[1].strip())
        elif temp == "what does the fox say?":
            break
        else:
            sound += temp.split()
        
    print(*[i for i in sound if i not in not_fox])


        