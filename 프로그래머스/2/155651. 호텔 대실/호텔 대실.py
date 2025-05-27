def time_diff_10min(a,b):
    h1,m1 = map(int,a.split(":"))
    h2,m2 = map(int,b.split(":"))
    min1 = h1*60+m1
    min2 = h2*60+m2
    return min1+10 <= min2
    
    
def solution(book_time):
        
    sort_time = sorted(book_time,key=lambda x: [x[0],x[1]])
    room,ans = [],0
    
    while sort_time:
        a,b = sort_time.pop(0)
        for i in range(len(room)):
            if time_diff_10min(room[i],a):
                room.pop(i)
                room.append(b)
                break                                
        else:
            ans +=1
            room.append(b)

        room.sort()
    return ans