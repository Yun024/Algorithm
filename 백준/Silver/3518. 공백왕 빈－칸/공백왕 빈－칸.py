import sys

strings = sys.stdin.read().strip().split("\n")
S = [s.split() for s in strings]
length = max([len(s.split()) for s in strings])

strings = [s.split() for s in strings]
for s in strings:
    while len(s) != length:
        s.append("")

temp = []
for l in range(length):
    temp.append(max(len(i) for i in list(map(lambda x: x[l],strings))))

for s in strings:
    ans = []
    for word,leng in zip(s,temp):
        word += " " * (leng - len(word))
        ans.append(word)
    ans = [i for i in ans if i.strip()] 
    ans[-1] = ans[-1].strip()
    print(*ans)