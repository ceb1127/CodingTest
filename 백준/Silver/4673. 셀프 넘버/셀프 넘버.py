def self(n): #생성자구하기
    n = n+sum(map(int,str(n))) #각 자리 수 합 구해줌
    return(n)

list=[0]*10001  #리스트 크기 지정. 리스트를 0으로 초기화하고 10000개로 지정

#생성자 찾기
for i in range(1,10000+1) :
    list[i]=self(i)

#생성자라면 리스트 추가하고 출력하기
for i in range(1,10000+1) :
    if i not in list :
        print(i)