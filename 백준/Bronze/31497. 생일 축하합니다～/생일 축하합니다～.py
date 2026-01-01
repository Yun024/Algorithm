import sys
input = sys.stdin.readline

n = int(input().strip())
names = [input().strip() for _ in range(n)]
ans = []

for name in names:
    sys.stdout.write(f"? {name}\n")
    sys.stdout.flush()
    res1 = int(input().strip())

    sys.stdout.write(f"? {name}\n")
    sys.stdout.flush()
    res2 = int(input().strip())

    if res1 + res2 == 2:
        sys.stdout.write(f"! {name}")
        break
    elif res1 + res2 == 1:
        ans.append(name)
else:
    sys.stdout.write(f"! {ans[0]}")
    sys.stdout.flush()