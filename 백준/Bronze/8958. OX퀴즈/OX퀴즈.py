num = int(input()) #테스트 케이스 개수 입력

for j in range(num) : 
    result = list(str(input())) #결과를 리스트로

    cnt = 0 #"O" 개수
    score = 0 # 총합

    for i in result :
        
        if i == 'X' :
            cnt = 0 #'X' 다음 'O' 점수 계산은 다시 처음부터
            score += 0

        else : 
            cnt += 1
            score += cnt
        
    print(score)