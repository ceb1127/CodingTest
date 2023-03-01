def solution(absolutes, signs):
    answer = 0
    result = []
    
    for i in range(len(signs)) :
        if signs[i] == True :
            result.append(int(str(absolutes[i])))
        elif signs[i] == False :
            result.append(int('-'+str(absolutes[i])))
        
    answer = sum(result)
        
    return answer