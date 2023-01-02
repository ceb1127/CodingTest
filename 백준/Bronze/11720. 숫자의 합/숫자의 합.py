#문자열로 입력받아서 분리해서 더하기 
sum=0
N = int(input()) #수 입력

a_list = list(input()) #입력받은 값 분리해서 리스트

for i in range(N) :
    sum += int(a_list[i]) #리스트 값 더하기

print(sum)