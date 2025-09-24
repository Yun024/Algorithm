import sys
lv, score = sys.stdin.readline().split()

if score == "miss":
    print("0")
elif score == 'bad':
    print(int(lv)*200)
elif score == 'cool':
    print(int(lv)*400)
elif score == 'great':
    print(int(lv)*600)
else:
    print(int(lv)*1000)