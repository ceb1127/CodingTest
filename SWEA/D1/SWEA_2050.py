# 2050. 알파벳을 숫자로 변환 D1
N = input()
for i in range(len(N)):
    NtoInt = ord(N[i])-64
    print(NtoInt,end=" ")
