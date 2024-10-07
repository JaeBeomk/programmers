# https://school.programmers.co.kr/learn/courses/30/lessons/340213
# 동영상재생기
# 10초전 이동 / 10초후 이동/ 오프닝 건너뛰기

def solution(video_len, pos, op_start, op_end, commands):
    # 현재 위치 pos ->> command 
    
        
    pos_min=pos.split(":")
    pos_sec=int(pos_min[0])*60 + int(pos_min[1])
    
    open=op_start.split(":")
    open_sec=int(open[0])*60+int(open[1])
    opend=op_end.split(":")
    opend_sec=int(opend[0])*60+int(opend[1])
    
    if pos_sec in range(open_sec,opend_sec): pos_sec=opend_sec
    for i in commands:
        
        if i == "next": pos_sec +=10
        elif i == "prev": 
            pos_sec-=10
            if pos_sec <=0: pos_sec=0
        if pos_sec in range(open_sec,opend_sec): pos_sec=opend_sec
            
    min=pos_sec//60
    sec=pos_sec%60
    min_s=str(min)
    sec_s=str(sec)
    
    answer=min_s.zfill(2)+":"+sec_s.zfill(2)
    return answer

print(solution("34:33","13:00","00:55","02:55",["next", "prev"])) #"13:00"
print(solution("10:55","00:05","00:15","06:55",["prev", "next", "next"])) #"06:55"
print(solution("07:22",	"04:05"	,"00:15"	,"04:07",["next"])) #"04:17"


# 나중에 다시 풀기
