T = int(input())

for _ in range(T) :
    floor = int(input()) #층 
    num = int(input()) #호

    floor_0 = [x for x in range(1,num+1)  ] # 0층 리스트

    for k in range(floor) : # 층 수 만큼 반복
        for i in range(1,num) : # 1 ~ n-1 까지 (인덱스)
            floor_0[i] += floor_0[i-1] # 층별 각 호실의 사람 수를 변경

    # print(floor_0) #해당 층 수 호실까지 인원 다 출력
    print(floor_0[-1]) #가장 마지막 수 출력