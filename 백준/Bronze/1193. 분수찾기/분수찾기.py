X = int(input())    # 14

line = 1

while X > line : 
    X -= line       # x = 14, 13, 11, 8, 4
    line += 1       # line = 1, 2, 3, 4, 5

if line%2 == 0 : # 짝수 라인일 경우
    a = X
    b = line - X + 1

else : # 홀수 라인일 경우
    a = line - X + 1
    b = X

print(a, "/" , b, sep="")