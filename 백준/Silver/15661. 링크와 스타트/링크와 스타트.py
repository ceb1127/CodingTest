# 백트래킹 -> 스타트와링크에서 n/2 없음
def go(index, first, second) :
    if index == n:
        if len(first) == 0:
            return -1
        if len(second) == 0:
            return -1
        t1 = 0
        t2 = 0
        for p1 in first :
            for p2 in first :
                if p1 == p2 :
                    continue
                t1 += s[p1][p2]
        for p1 in second:
            for p2 in second:
                if p1 == p2:
                    continue
                t2 += s[p1][p2]
        diff = abs(t1-t2)
        return diff
    
    ans = -1
    # 1팀
    t1 = go(index+1, first+[index], second)
    if ans == -1 or (t1 != -1 and ans > t1):
        ans = t1
    # 2팀
    t2 = go(index+1, first, second+[index])
    if ans == -1 or (t2 != -1 and ans > t2 ):
        ans = t2
    return ans 

n = int(input())
s = [list(map(int,input().split())) for _ in range(n) ]
print(go(0,[],[]))