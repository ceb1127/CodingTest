def solution(arr, divisor):
    answer = []
    arr = sorted(arr)

    for i in arr :
        if i % divisor == 0:
            answer.append(i)
            answer.sort()

    if len(answer) == 0 : 
        answer.append(-1)
    
    return answer
            