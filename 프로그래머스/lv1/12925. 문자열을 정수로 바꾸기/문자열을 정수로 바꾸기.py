def solution(s):
    s = list(s)
    answer = ""
    if s[0] != '+' and s[0] != '-' :
        for i in range(len(s)) :
            answer += str(int(s[i]))
        return int(answer)
    else :
        for i in range(1,len(s)) :
            answer += str(int(s[i])) 
        return int(s[0]+ answer)