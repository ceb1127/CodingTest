word = [input() for _ in range(5)]

for i in range(15):
    for j in range(5):
        if i < len(word[j]) : #행 길이가 열의 길이보다 작으면
            print(word[j][i], end="")