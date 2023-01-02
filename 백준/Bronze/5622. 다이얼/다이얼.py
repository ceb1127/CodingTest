import sys
input=sys.stdin.readline

# 다이얼 넘버
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

#알파벳 입력
li = list(input())

#걸리는 시간
time = 0

for i in li :
    for j in dial :
        # 만약에 입력받은 값이 Number에 있으면 index에서 3초를 더해준다.
        if i in j :
            time += dial.index(j) + 3


print(time)