a = []
while 1:
    try:
        a.append(int(input()))
    except:
        break
print(max(a),a.index(max(a))+1)