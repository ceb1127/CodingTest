def solution(s):
    answer = 0
    cnt_notx = 0
    cnt_x = 0
    
    for i in s:
        if cnt_notx == cnt_x :
            answer += 1
            su = i
        if su == i:
            cnt_x += 1
        else :
            cnt_notx +=1
            
    return answer