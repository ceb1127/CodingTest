N = int(input())

#함수
def hansu(N):
    cnt = 0  #한수 개수 세는 변수

    for i in range(1, N+1) :
        if i < 100 : #두자리수 . 두 자리 수는 모두 한수
            cnt += 1
        elif i >= 100 :
            hansu_list = list(map(int,str(i)))
            if hansu_list[1] == (hansu_list[0] + hansu_list[2]) / 2 : #등차수열일 결루 성립하는 공식
                cnt += 1
        else:
            pass
    return cnt

print(hansu(N))