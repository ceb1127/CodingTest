# 2056. 연원일 달력 D1
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    cal = str(input())
    year = cal[:3+1]
    month = cal[4:5+1]
    day = cal[6:]
    days = {1:31, 2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    fail = -1
    if 1<= int(month) <= 12 and int(day) <= days[int(month)] :
        print("#{} {}/{}/{}".format(test_case,year,month,day))
    else:
        print(-1)