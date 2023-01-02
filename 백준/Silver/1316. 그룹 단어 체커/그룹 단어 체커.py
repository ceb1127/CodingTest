N = int(input()) #단어의 개수 입력

for _ in range(N) :
    word = input()

    for i in range(len(word)-1) : # 단어 길이만큼 반복
        if word[i] == word[i+1] : # 알파벳 앞뒤가 같으면 pass
            pass
        elif word[i] in word[i+1:] : # 지금 위치 알파벳이 
            N -= 1 #입력받은 단어 수에서 하나씩 뺀다
            break
print(N)