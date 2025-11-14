import sys
input = sys.stdin.readline

pop_word = input().strip()
input_word = input().strip()

ans = ""
for word in input_word:
    if word not in pop_word:
        ans += word

print(ans)