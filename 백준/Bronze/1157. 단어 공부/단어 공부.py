
word = input().upper() # 단어 입력받아서 대문자로 전환 ex)baekjoon
searchKeys = list(set(word))# 단어 요소 검색 키들을 따로 리스트로 만들어 놓음 .set으로 중복 제거 ex)['B', 'J', 'K', 'A', 'E', 'O', 'N']

countArr = [] # 알파벳 개수를 담을 리스트
for key in searchKeys : 
    countArr.append(word.count(key)) #ex)[1, 1, 1, 1, 1, 1, 2]

if countArr.count(max(countArr)) > 1 :
    print("?")
else : 
    print(searchKeys[countArr.index(max(countArr))])