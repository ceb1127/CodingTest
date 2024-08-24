N, M = map(int,input().split())

chess = []
str1 = "WBWBWBWB"
str2 = "BWBWBWBW"
pivot1 = [ str1, str2, str1, str2, str1, str2, str1, str2 ]
pivot2 = [ str2, str1, str2, str1, str2, str1, str2, str1 ]

result = float('inf')  # 결과를 무한대로 초기화

for _ in range(N): 
    chess.append(input().strip())

for i in range(N-8+1):
    for j in range(M-8+1):
        cnt1 = 0
        cnt2 = 0
        for p in range(8):
            for q in range(8):
                if chess[i+p][j+q] != pivot1[p][q] :
                    cnt1 += 1
                if chess[i+p][j+q] != pivot2[p][q] :
                    cnt2 += 1
        result = min(result, cnt1, cnt2)

print(result)
                

    