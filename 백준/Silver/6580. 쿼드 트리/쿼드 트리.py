import sys
input = sys.stdin.readline

def quadtree(r,c,n):
    if n == 1:
        return 'B' if xbm[r][c] == '1' else 'W'
    
    pixels = set()
    for i in range(r,r+n):
        pixels.update(xbm[i][c:c+n])
        if len(pixels) > 1:
            break
    
    if len(pixels) == 1:
        color = pixels.pop()
        return 'B' if color == '1' else 'W'
    
    half = n//2
    result = ''.join([
        quadtree(r,c,half),
        quadtree(r,c+half,half),
        quadtree(r+half,c,half),
        quadtree(r+half,c+half,half)
    ])      
    return 'Q' + result

n = int(input().split()[-1])
for _ in range(2):
    input()

xbm = []
dic = {"a":10,"b":11,"c":12,"d":13,"e":14,"f":15}

for _ in range(n):
    hexa = ""
    for temp in input().strip()[:-1].split(","):
        oct = ""
        for tmp in temp[2:]:
            oct += bin(int(dic.get(tmp,tmp)))[2:].zfill(4)
        hexa += oct[::-1]
    xbm.append(hexa)
            
print(str(n) + '\n'+quadtree(0,0,n))