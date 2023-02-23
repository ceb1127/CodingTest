# select 방법
# index : 수 index
# selected : 선택한 수의 개수
N, M = map(int, input().split())
a = [0]*M

def go(index, selected, N, M):
    if selected == M :
        print(' '.join(map(str,a)))
        return
    
    if index > N : # 더이상 선택할 수 없음. -> 종료
        return

    # 선택
    a[selected] = index
    go(index+1, selected+1, N,M)
    # 선택x
    a[selected] = 0
    go(index+1, selected,N,M) # 선택하지않았으니 selected는 변하지 않음

go(1,0,N,M)
