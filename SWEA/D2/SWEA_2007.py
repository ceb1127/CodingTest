#2007 패턴 마디의 길이 D2
T = int(input())
for test_case in range(1,T+1):
    word = str(input())
    count = 0
    for i in range(1,30) :
        if word[i] == word[0]:
            if word[:i] == word[i:i*2] :
                count = len(word[i:i*2])
                #print(word[i:i*2])
                print("#{} {}".format(test_case,count))
                break

