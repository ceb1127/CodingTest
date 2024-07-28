S = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
result = []

for i in range(len(alpha)):
    if alpha[i] in S :
        result.append(S.index(alpha[i]))
    else :
        result.append(-1)
        
for i in range(len(result)):
    print(result[i], end=" ")


    