# # "6의 배수" 로 늘어나는 벌집 -> whlie문으로 입력받은 수인 n에 도달할 때 까지만 반복
# 반복문이 반복되는 동안에 반복횟수를 카운트해서 이 카운트 한 숫자를 마지막에 출력


n = int(input())
nums_pileup = 1 # 벌집 개수 1부터 시작해서 6의 배수 증가
cnt = 1 # 반복문이 반복되는 횟수 카운트

while n > nums_pileup :
    nums_pileup += 6 * cnt 
    cnt += 1

print(cnt)
