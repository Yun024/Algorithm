import sys
from itertools import combinations
input = sys.stdin.readline



def get_score(card1, card2):
    if card1 == card2:
        return 100 + card1  # 땡
    else:
        return (card1 + card2) % 10  # 끗

a, b = map(int, input().split())  # 영학이의 패

cards = []
for i in range(1, 11):
    cards.extend([i, i])  # 각 숫자 2장씩

cards.remove(a)
cards.remove(b)

total = 0
win = 0

for x, y in combinations(cards, 2):
    total += 1
    me = get_score(a, b)
    you = get_score(x, y)

    if me > you:
        win += 1

print("{:.3f}".format(win / total))
