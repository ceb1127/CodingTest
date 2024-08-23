N = int(input())
cnt = 0
su = 666 

while True :
    if '666' in str(su):
        cnt+=1
    if cnt == N : 
        print(su)
        break

    su += 1