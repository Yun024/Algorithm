answer = [input() for i in range(5)]
ans = []

max_len = max([len(i) for i in answer])
answer = [i.ljust(max_len,' ') for i in answer]

print(''.join([''.join([j[i] for j in answer if j[i] != ' ']) for i in range(max_len)]))