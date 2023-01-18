def solution(n):
    n_list = sorted(list(map(int,str(n))),reverse = True)
    answer = int(''.join(str(i) for i in n_list ))
    return answer