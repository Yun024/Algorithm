import sys
input = sys.stdin.readline

alphabet = 'abcdefghijklmnopqrstuvwxyz'
input_word = input().split("\n")[0]
key_word = input().strip()
num = 0
length = len(key_word)
ans = ""

for word in input_word:
    if word != " ":
        ans += alphabet[alphabet.index(word) - alphabet.index(key_word[num%length]) - 1]
    else:
        ans += " "
    num += 1
print(ans)