sugar = int(input())

bag = 0
while sugar >= 0:
    if sugar % 5 == 0 : # 5의 배수이면
        bag += (sugar//5) # 5로 나눈 몫 더해줌
        print(bag)
        break
    sugar -= 3
    bag += 1 # 5의 배수가 될 때까지 설탕-3, 봉지 +1
else :
    print(-1)