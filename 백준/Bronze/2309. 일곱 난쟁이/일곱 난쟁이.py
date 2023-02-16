# combination 라이브러리 활용 9C2
from itertools import combinations

nanjaeng = [int(input()) for i in range(9)]
occation = list(combinations(nanjaeng,7))
for i in occation:
    if sum(i) == 100 :
        answer = list(i)
        break
answer.sort()
print(*answer,sep='\n')