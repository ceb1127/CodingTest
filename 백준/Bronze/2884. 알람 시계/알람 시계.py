H, M = map(int,input().split())

if M < 45 :
    if H > 0 :
        print(H-1, M+60-45)
    if H == 0 :
        print(H+23, M+60-45)
else :
    print(H, M-45)