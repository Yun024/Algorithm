import sys
from itertools import permutations

ln = int(sys.stdin.readline().strip())
board = [line.split() for line in sys.stdin]
visited = [True] * ln
final = []

def backtrack(ln, visited, answer=[]):
    if len(answer) == ln//2:
        global final
        final.append(answer)
        return

    for i in range(ln):
        if visited[i] and (not answer or answer[-1] < i):
            temp = answer.copy()
            temp.append(i)
            visited[i] = False
            backtrack(ln, visited, temp)
            visited[i] = True

backtrack(ln,visited)
final

def team_power(team, board):
    answer = 0
    for i in list(permutations(team,2)):
        answer += int(board[i[0]][i[1]])
    return answer

ans = []
dupl = set([i for i in range(ln)])
for i in final[:len(final)//2]:
    start = team_power(i,board)
    link = team_power(dupl - set(i),board)
    ans.append(abs(start - link))
    
print(min(ans))