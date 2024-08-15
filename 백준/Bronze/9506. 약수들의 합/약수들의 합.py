while True: 
    num = int(input())
    num_list = []
    
    if num == -1 :
        break
    
    for i in range(1,num):
        if num % i == 0 :
            num_list.append(i)
    if sum(num_list) == num : 
        print(num, ' = ', " + ".join(str(i) for i in num_list), sep = '')
    else:
        print(num, 'is NOT perfect.')
