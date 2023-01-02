coin_list = [500, 100, 50, 10, 5, 1]
count = 0

price = int(input())
change = 1000 - price

for i in coin_list :
    count += change // i
    change %= i

print(count)