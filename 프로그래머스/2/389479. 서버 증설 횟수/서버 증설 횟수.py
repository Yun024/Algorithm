def solution(players, m, k):
    
    ans = 0
    server = [0] * 24
    for i in range(24):
        plus = players[i]//m - server[i]
        if plus > 0:
            ans += plus
            for n in range(k):
                if i+n >= 24:
                    break
                server[i+n] += plus
    return ans