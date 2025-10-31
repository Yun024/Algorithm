import sys

alphabet = sys.stdin.readline().strip()
ans = (ord(alphabet) - ord("I") if alphabet > "I" else ord("I") - ord(alphabet)) + 84
print(ans)