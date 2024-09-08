import sys

input = sys.stdin.readline

def fibonacchi(n):
    n_list = [0]*(n+1)
    n_list[0] = 0
    n_list[1] = 1

    for i in range(2,n+1):
        n_list[i] = n_list[i-1] + n_list[i-2]

    return n_list[n]

n = int(input())
print(fibonacchi(n))