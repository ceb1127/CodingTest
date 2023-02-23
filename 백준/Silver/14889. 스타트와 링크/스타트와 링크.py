# 백트래킹 : 브루트포스 + 더이상의 함수 호출이 의미 없을 경우
def go(index, first, second):
    if index == n:
        if len(first) != n//2 : #2/n이 아닐 경우 백트래킹
            return -1
        if len(second) != n//2 :
            return -1
        t1 = 0
        t2 = 0
        for i in range(n//2) :
            for j in range(n//2):
                if i == j:
                    continue
                t1 += s[first[i]][first[j]]
                t2 += s[second[i]][second[j]]
        diff = abs(t1-t2)
        return diff
    
    ans = -1
    # 1번
    t1 = go(index+1, first+[index], second)
    if ans == -1 or (t1 != -1 and ans > t1):
        ans = t1
    # 2번
    t2 = go(index+1, first, second+[index])
    if ans == -1 or (t2 != -1 and ans > t2):
        ans = t2
    return ans



n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]
print(go(0,[ ],[ ]))
