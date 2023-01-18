def solution(a, b):
    answer = 0
    min_num, max_num = min(a,b), max(a,b)
    for i in range(min_num,max_num+1) : 
        answer += i
    return answer