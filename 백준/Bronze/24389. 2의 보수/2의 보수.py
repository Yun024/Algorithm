import sys
n = int(sys.stdin.readline().strip())

before = bin(n)[2:].zfill(32)
after = int(''.join([str((int(b)+1)%2) for b in before]),2)+1

print(sum([int(i) for i in bin(n^after)[2:]]))
