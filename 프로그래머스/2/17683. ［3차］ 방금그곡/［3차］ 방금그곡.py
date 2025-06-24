from datetime import datetime
def solution(m, musicinfos):
    
    def time_diff(start,end):
        fmt = "%H:%M"
        t1 = datetime.strptime(start,fmt)
        if start.split(":")[0] > end.split(":")[0]:
            t2 = datetime.strptime("24:00",fmt)
        else:
            t2 = datetime.strptime(end,fmt)
        return int((t2-t1).total_seconds())//60
    
    def find_token(melody):
        i = 0
        token = []
        while i < len(melody):
            if melody[i] == "#":
                token[-1] += "#"
            else:
                token.append(melody[i])
            i +=1
        return token
    
    def melody_repeat(melody,rpt):
        
        melody_token = find_token(melody)
        num = len(melody_token)
        return (melody_token * (rpt//num +1))[:rpt+1]
            
    def find_title(m,melody_token):
        m_token = find_token(m)
        for i in range(len(melody_token) - len(m_token) + 1):
            if melody_token[i:i+len(m_token)] == m_token:
                return True
        return False
    
    def find_answer(music):
        if not music:
            return "(None)"
        max_n = max([i[1] for i in music])
        ans = [i for i in music if i[1] == max_n]
        return ans[0][0]
    
    musicinfos = sorted(musicinfos,key=lambda x: x.split(",")[0])
    music = []
    for musicinfo in musicinfos:
        start,end,title,melody = musicinfo.split(",")
        rpt = time_diff(start,end)
        melody_token = melody_repeat(melody,rpt)
        if find_title(m,melody_token):
            music.append([title,rpt])
    answer = find_answer(music)
    
    return answer