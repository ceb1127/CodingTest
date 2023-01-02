n = int(input()) #테스트 케이스 수 입력

for i in range(n) : 
    cnt, word = input().split() #반복할 수랑 문자열 입력
    for x in word : 
        print(x*int(cnt), end="") #end=" 옆으로 붙임
    print() #줄넘김