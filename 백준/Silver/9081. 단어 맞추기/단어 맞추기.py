import sys
input = sys.stdin.readline

n = int(input().strip())
for _ in range(n):
    s = input().strip()
    temp = [ord(i) for i in s]
    for i in range(len(s)-1,0,-1):
        if temp[i] > temp[i-1]:
            temp1,temp2 = temp[i-1], min([j for j in temp[i:] if j > temp[i-1]])
            temp[i-1] = temp2
            front = temp[:i]
            back = temp[i:]
            back.remove(temp2)
            back.append(temp1)
            ans = front + sorted(back)
            print(''.join([chr(j) for j in ans]))
            break
    else:
        print(s)