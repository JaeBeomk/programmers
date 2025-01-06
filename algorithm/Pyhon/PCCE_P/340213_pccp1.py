# https://school.programmers.co.kr/learn/courses/30/lessons/340213
# 동영상재생기
# 10초전 이동 / 10초후 이동/ 오프닝 건너뛰기

def get_total_sec(str):
    return int(str[0:2])*60 + int(str[3:])

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    total_sec = get_total_sec(video_len)
    if op_start <= pos and pos <= op_end:
        pos = op_end
    pos_sec = get_total_sec(pos)
    for command in commands:
        if command == "next":
            pos_sec += 10
            if total_sec < pos_sec:
                pos_sec = total_sec
        elif command == "prev":
            pos_sec -= 10
            if pos_sec < 0:
                pos_sec = 0
        if get_total_sec(op_start) <= pos_sec and pos_sec <= get_total_sec(op_end):
            pos_sec = get_total_sec(op_end)

    min = str(pos_sec // 60)
    if len(min) < 2:
        min = "0" + min

    sec = str(pos_sec % 60)
    if len(sec) < 2:
        sec = "0" + sec

    answer = min + ":" + sec

    return answer


print(solution("34:33","13:00","00:55","02:55",["next", "prev"])) #"13:00"
print(solution("10:55","00:05","00:15","06:55",["prev", "next", "next"])) #"06:55"
print(solution("07:22",	"04:05"	,"00:15"	,"04:07",["next"])) #"04:17"





# 나중에 다시 풀기
