def solution(t, p):
    answer = 0
    
    su = [t[i:i+len(p)] for i in range(0, len(t)) if len(t[i:i+len(p)]) == len(p)]
    list_su = list(map(int, su))
    
    for t in list_su :
        if t <= int(p):
            answer += 1
    return answer