
import sys

input = sys.stdin.readline
max_su = 1000000

def eratosthenes():
    sosu = [True]*(max_su+1)
    sosu[0] = sosu[1] = False

    for i in range(2, int(max_su**0.5)+1 ):
        if sosu[i]: # 소수인지 확인
            for j in range(i*i,max_su+1,i): #배수를 지움
                sosu[j] = False

    while True:
        n = int(input())
        if n == 0 :
           break
        
        for i in range(3,n):
            if sosu[i] and sosu[n-i] : 
                print(f"{n} = {i} + {n-i}")
                break
        else: 
            print("Goldbach's conjecture is wrong.")




eratosthenes()



            







    



