def solution(video_len, pos, op_start, op_end, commands):
    for i in commands:
        if pos >= op_start and pos <= op_end :
            pos = op_end
            
        mi,ss = int(pos[:2]), int(pos[3:])
        
        if i == 'next' :
            mi += (ss+10)//60 
            ss = (ss+10)%60
            pos = min(video_len, str(mi).zfill(2) + ':' + str(ss).zfill(2))
                           
        if i == 'prev':
            if '00:10' > pos:
                pos = '00:00'
            else:
                mi = mi-1 if (ss+50) < 60 else mi
                ss = (ss+50)%60
                pos = str(mi).zfill(2) + ':' + str(ss).zfill(2)
                
        if pos >= op_start and pos <= op_end :
            pos = op_end
        
    return pos