from datetime import datetime

class MusicMatcher:
    def __init__(self, m, musicinfos):
        self.query = m
        self.musicinfos = sorted(musicinfos,key = lambda x: x.split(",")[0])
    
    def find_token(self,melody):
        i = 0
        tokens = []
        while i < len(melody):
            if melody[i] == "#":
                tokens[-1] += "#"
            else:
                tokens.append(melody[i])
            i +=1
        return tokens
        
    def time_diff(self,start,end):
        fmt = "%H:%M"
        t1 = datetime.strptime(start,fmt)
        t2 = datetime.strptime(end,fmt)
        return int((t2-t1).total_seconds()) //60
    
    def find_full_melody(self,melody,length):
        rpt = length//len(melody) + 1
        return (melody * rpt)[:length]
    
    def find_title(self,m,full_melody):
        query_length = len(m)
        for i in range(len(full_melody) - query_length + 1):
            if full_melody[i:i+query_length] == m:
                return True
        return False
    
    def find_answer(self,answer):
        if not answer:
            return "(None)"
        max_streaming = max([i[1] for i in answer])
        return [i[0] for i in answer if i[1] == max_streaming][0]
        
    def solve(self):
        m_token = self.find_token(self.query)
        answer = []
        
        for musicinfo in self.musicinfos:
            start,end,title,melody = musicinfo.split(",")
            melody_token = self.find_token(melody)
            length = self.time_diff(start,end)
            full_melody_token = self.find_full_melody(melody_token,length)
            if self.find_title(m_token,full_melody_token):
                answer.append([title,length])
        # return self.find_answer(answer)
        return self.find_answer(answer)
                
def solution(m,musicinfos):
    matcher = MusicMatcher(m,musicinfos)
    return matcher.solve()
        