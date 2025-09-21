import sys
input = sys.stdin.readline

promise = ['Never gonna give you up', 'Never gonna let you down', 'Never gonna run around and desert you', 'Never gonna make you cry', 'Never gonna say goodbye', 'Never gonna tell a lie and hurt you',
'Never gonna stop']

n = int(input().strip())
for _ in range(n):
    if input().strip() not in promise:
        print('Yes')
        break
else:
    print('No')
