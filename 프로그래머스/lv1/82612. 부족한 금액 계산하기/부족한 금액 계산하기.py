def solution(price, money, count):
    answer = 0
    result = 0
    
    for i in range(1,count+1) :
        result += price*i
        if result > money :
            answer = result - money
    return answer