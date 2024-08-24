a = []
while 1:
    try:
        a.append(int(input()))
    except:
        break
print(len(set([i%42 for i in a])))
        


